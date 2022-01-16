from django.urls import path
from django.conf.urls import include
from .views.home import index
from .views.register import Signup
from .views.login import Login, logout
from .views.products import Products
from .views.search import Search
from .views.product_desp import product_detail
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.help import HelpView
from .views.contact import Contact
from .middlewares.auth import auth_middleware
from .views.terms import Terms
from .views.privacy import Privacy
from .views.payment import Payment


urlpatterns = [
    path('', index,  name='homepage'),
    path('product/', Products.as_view(), name='product'),
    path('search/', Search.as_view(), name='search'),
    path('register/', Signup.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out/', CheckOut.as_view() , name='checkout'),
    path('payment/', Payment, name='payment'),
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
    path('help/', HelpView.as_view(), name='help'),
    path('contact/', Contact, name='contact'),
    path('privacy/', Privacy, name='privacy'),
    path('terms/', Terms, name='terms'),
    path('description/<int:id>/', product_detail, name='product_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
