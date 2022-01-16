from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View

class Search(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('search')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
            request.session['cart'] = {}
        products = None
        q=request.GET['q']
        if q:
            products = Product.get_all_products_by_product_name(q)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        print(data)
        print('you are : ', request.session.get('email'))
        return render(request, 'search.html', data)

