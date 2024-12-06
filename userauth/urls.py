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
    path('usermanagement/', views.user_management, name='usermanagement'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('view_user/<int:id>/', views.view_user, name='view_user'),
    path('view_post/<int:id>/', views.view_post, name='view_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('authorinfo/', views.authorinfo, name='authorinfo'),
    path('Settings/', views.Settings, name='Settings'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
]
