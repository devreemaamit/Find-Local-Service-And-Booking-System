from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ProviderService, ServiceCategory
from accounts.decorators import provider_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from django.shortcuts import render
from .models import ProviderService
from reviews.models import Review
from django.db.models import Avg, Q
from django.db.models.functions import Coalesce
from django.db.models import Value, FloatField

@login_required
def create_or_edit_category(request, pk=None):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Only admin can manage service categories.")

    category = get_object_or_404(ServiceCategory, pk=pk) if pk else None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if category:
            category.name = name
            category.description = description
            category.save()
        else:
            ServiceCategory.objects.create(name=name, description=description)

        return redirect('list_categories')

    return render(request, 'admin/create_category.html', {
        'category': category,
        'is_edit': pk is not None
    })

@login_required
def list_categories(request):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Only admin can view service categories.")
    categories = ServiceCategory.objects.filter(is_active=True)
    return render(request, 'admin/list_categories.html', {'categories': categories})

@login_required
def delete_category(request, pk):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Only admin can delete service categories.")
    category = get_object_or_404(ServiceCategory, pk=pk)
    category.is_active = False
    category.save()
    return redirect('list_categories')


# Provider Views Their Services
@provider_required
def provider_services(request):
    services = ProviderService.objects.filter(provider=request.user, is_active=True)
    return render(request, 'services/provider_services.html', {'services': services})


# Provider Adds and edit Services
@provider_required
def create_or_edit_service(request, pk=None):
    categories = ServiceCategory.objects.all()
    service = get_object_or_404(ProviderService, pk=pk, provider=request.user) if pk else None

    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')

        if service:
            service.service_name = service_name
            service.category_id = category_id
            service.price = price
            service.description = description
            service.save()
        else:
            ProviderService.objects.create(
                provider=request.user,
                service_name=service_name,
                category_id=category_id,
                price=price,
                description=description
            )

        return redirect('provider_services')

    return render(request, 'services/add_service.html', {
        'service': service,
        'categories': categories,
        'is_edit': pk is not None
    })

@login_required
def delete_service(request, pk):
    service = get_object_or_404(ProviderService, pk=pk)
    # Allow provider to delete their own service, or admin to delete any service
    if request.user.role != 'provider' and request.user.role != 'admin':
        return HttpResponseForbidden("Only the service provider or admin can delete this service.")
    if request.user.role == 'provider' and service.provider != request.user:
        return HttpResponseForbidden("Providers can only delete their own services.")
    service.is_active = False  # Soft delete
    service.save()
    # Redirect based on who deleted
    if request.user.role == 'admin':
        return redirect('manage_providers')


@login_required
def view_bookings(request):
    # In real projects, you'd fetch bookings related to this user
    bookings = []  # placeholder for future logic
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

def server_up(request):
    return JsonResponse({"message": "Hello from Django Smart Service!","time": str(datetime.datetime.now())})

@login_required
def service_list(request):

    query = request.GET.get('q')

    services = ProviderService.objects.filter(
        is_active=True,
        is_available=True
    )

    if query:
        services = services.filter(
            Q(service_name__icontains=query) |
            Q(description__icontains=query) |
            Q(provider__full_name__icontains=query) |
            Q(provider__contact_number__icontains=query) |
            Q(provider__address__icontains=query) |
            Q(category__name__icontains=query)
        )

    # Average Rating
    services = services.annotate(
        avg_rating=Coalesce(
            Avg('bookings__review__rating'),
            Value(0.0),
            output_field=FloatField()
        )
    )

    # Round rating (important)
    for service in services:
        service.avg_rating = round(service.avg_rating, 1)

    return render(request, 'services/service_list.html', {
        'services': services
    })

@login_required
def service_detail(request, service_id):

    service = get_object_or_404(
        ProviderService,
        id=service_id,
        is_active=True
    )

    reviews = Review.objects.filter(
        booking__service=service,
        is_active=True
    )

    return render(request, 'services/service_detail.html', {
        'service': service,
        'reviews': reviews
    })


