from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:service_id>/', views.book_service, name='book_service'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('provider-bookings/', views.provider_bookings, name='provider_bookings'),
    path('update-status/<int:booking_id>/<str:status>/',
         views.update_booking_status,
         name='update_booking_status'),
]
