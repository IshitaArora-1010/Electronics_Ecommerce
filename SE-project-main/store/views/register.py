from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        address = postData.get('address')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            address=address)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'register.html', data)

    def validateCustomer(self, customer):
        SpecialSym = ['$', '@', '#', '%']
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif not any(char.isupper() for char in customer.password):
            error_message = 'Password must contain at least one uppercase letter'
        elif not any(char.islower() for char in customer.password):
            error_message = 'Password must contain at least one lowercase letter'
        elif not any(char.isdigit() for char in customer.password):
            error_message = 'Password must contain at least one digit'
        elif not any(char in SpecialSym for char in customer.password):
            error_message = 'Password must contain at least one special character($@#%)'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered.'
        # saving

        return error_message