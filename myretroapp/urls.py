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
    path('respect/<int:post_id>', views.respect_post, name = 'respect_post'),
    path('comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('daily', views.daily_question, name='daily_question'),
    path('daily/answer/<int:prompt_id>', views.submit_daily_answer, name='submit_daily_answer'),
]