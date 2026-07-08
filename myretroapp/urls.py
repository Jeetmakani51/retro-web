from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name = 'register_view'),
    path('register', views.register_view, name = 'register_view'),
    path('login', views.login_view, name = 'login_view'),
    path('home', views.home_view, name = 'home_view'),
    path('logout', views.logout_view, name = 'logout_view'),
    path('grindpost', views.create_grind_post, name = 'create_grind_post'),
    path('grindfeed', views.grind_feed, name = 'grind_feed'),
    path('respect/<int:post_id>', views.respect_post, name = 'respect_post')
]