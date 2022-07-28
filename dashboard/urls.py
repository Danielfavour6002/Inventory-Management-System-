
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_details, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('product/delete/<int:pk>/', views.product_delete, name = 'dashboard-product-delete' ),
    path('order/delete/<int:pk>/', views.order_delete, name = 'dashboard-order-delete' ),
    path('product/update/<int:pk>/', views.product_update, name = 'dashboard-product-update' ),
    path('order/status/<int:pk>/', views.order_status, name = 'dashboard-order-status' ),

]