from django.shortcuts import render

def Payment(request):
    return render(request, 'payment.html')
