from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
