# reviews/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking
from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
        status='completed'
    )

    # Prevent duplicate review
    if hasattr(booking, 'review'):
        messages.warning(request, "You already reviewed this service.")
        return redirect('user_bookings')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.reviewer = request.user
            review.save()

            messages.success(request, "Review submitted successfully!")
            return redirect('user_bookings')
    else:
        form = ReviewForm()

    return render(request, 'review/add_review.html', {
        'form': form,
        'booking': booking
    })
