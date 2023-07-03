from django.urls import path
from . import views

urlpatterns = [
    path('Blogs/', views.posts, name='blogs'),
    path('Antiques/', views.antiquities_post, name='antiques'),
    path('Destinations/', views.location_posts, name='location_posts'),
        path('create_post/', views.create_post, name='create_post'),
    path('create_tag/', views.create_tag, name='create_tag'),
     path('', views.old, name='old'),
     path('sancun/', views.sanctum, name='sanctum'),
    path('home/', views.home, name = 'home'),
    path('about/', views.abt, name = 'about'),
        path('post/<int:post_id>/', views.view_post, name='view_post'),
]
