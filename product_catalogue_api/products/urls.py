from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_view, name='product_list_create_view'),
    path('detail/<int:pk>/', views.product_list_create_view, name='product_list_create_view'),
    path('update/<int:pk>/', views.product_update_delete_view, name='product_update_delete_view'),
    path('delete/<int:pk>/', views.product_update_delete_view, name='product_update_delete_view'),
]