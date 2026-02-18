from django.urls import path
from . import views

urlpatterns = [
    path('admin/create-category/', views.create_or_edit_category, name='create_category'),
    path('admin/categories/', views.list_categories, name='list_categories'),
    path('admin/edit-category/<int:pk>/', views.create_or_edit_category, name='edit_category'),
    path('admin/delete-category/<int:pk>/', views.delete_category, name='delete_category'),

    path('add', views.create_or_edit_service, name='add_service'),
    path('edit/<int:pk>', views.create_or_edit_service, name='edit_service'),
    path('delete-service/<int:pk>', views.delete_service, name='delete_service'),
    path('list', views.provider_services, name='provider_services'),
    
    path('my-bookings/', views.view_bookings, name='view_bookings'),
    path('api/serverup', views.server_up, name='serverup'),
    path('', views.service_list, name='service_list'),
    path('detail/<int:service_id>/',views.service_detail,name='service_detail'),


]
