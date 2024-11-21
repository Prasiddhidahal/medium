from django.urls import path
from . import views

app_name = 'medium'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<id>/', views.edit, name='edit'),
    path('view/<id>/', views.view, name='view'),
    path('delete/<id>/', views.delete, name='delete'),
    path('create/', views.create_blog, name='create_blog'),

]