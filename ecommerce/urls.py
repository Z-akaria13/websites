from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'ecommerce'

urlpatterns = [
     path('login/', views.login_view, name='login'),
   path('', views.product_list, name='product_list'),
    path('place_order/', views.place_order, name='place_order'),
    path('create_product/', views.create_product, name='create_product'),
        path('make_payment/', views.make_payment, name='make_payment'),
]