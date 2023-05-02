from django.urls import path
from . import views

app_name = 'cerebrum'

urlpatterns = [
   path('', views.home, name='home'),
       path('submit_text/', views.submit_text, name='submit_text'),
]