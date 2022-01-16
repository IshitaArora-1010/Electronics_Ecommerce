from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View

class ProductDescription(View):
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
        return redirect('product_detail')

def product_detail(request,id):
        # productID = request.GET.get('product')
        productID = Product.objects.get(pk=id)
        print("ID", productID)
        # products = Product.get_products_by_id(productID)
        # print("products", products)
        data={'product' : productID}
        return render(request, 'description.html', data)
   