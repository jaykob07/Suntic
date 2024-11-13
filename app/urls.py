from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', views.document_list, name='document_list'),
    path('create/', views.document_create, name='document_create'),
    path('update/<int:pk>/', views.document_update, name='document_update'),
    path('delete/<int:pk>/', views.document_delete, name='document_delete'),
    path('approve/<int:pk>/', views.document_approve, name='document_approve'),
]
