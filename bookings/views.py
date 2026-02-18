from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import ProviderService
from .models import Booking
from .forms import BookingForm
from django.contrib import messages


# USER BOOK SERVICE
@login_required
def book_service(request, service_id):
    service = get_object_or_404(ProviderService, id=service_id)

    # Check existing active booking
    existing_booking = Booking.objects.filter(
        user=request.user,
        service=service,
        status__in=['pending', 'confirmed']
    ).exists()

    if existing_booking:
        messages.error(
            request,
            "You already have an active booking for this service."
        )
        return redirect('user_bookings')

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.provider = service.provider
            booking.service = service
            booking.save()

            messages.success(request, "Booking confirmed successfully!")
            return redirect('user_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_service.html', {
        'form': form,
        'service': service
    })



# USER VIEW BOOKINGS
@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user,
        is_active=True
    ).select_related('service', 'service__category', 'provider')

    return render(request, 'bookings/user_bookings.html', {
        'bookings': bookings
    })


# PROVIDER VIEW BOOKINGS
@login_required
def provider_bookings(request):
    bookings = Booking.objects.filter(provider=request.user)
    return render(request, 'bookings/provider_bookings.html', {
        'bookings': bookings
    })


# UPDATE BOOKING STATUS
@login_required
def update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user == booking.provider:
        booking.status = status
        booking.save()

    return redirect('provider_bookings')

