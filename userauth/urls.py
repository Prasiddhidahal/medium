from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('baseadmin/', views.baseadmin, name='baseadmin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adminnavbar/', views.adminnavbar, name='adminnavbar'),
    path('usermanagement/', views.usermanagement, name='usermanagement'),
    path('authorinfo/', views.authorinfo, name='authorinfo'),
]
