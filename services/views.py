from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ProviderService, ServiceCategory
from accounts.decorators import provider_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import ServiceCategory
from django.http import JsonResponse
import datetime

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
    categories = ServiceCategory.objects.all()
    return render(request, 'admin/list_categories.html', {'categories': categories})

@login_required
def delete_category(request, pk):
    if request.user.role != 'admin':
        return HttpResponseForbidden("Only admin can delete service categories.")
    category = get_object_or_404(ServiceCategory, pk=pk)
    category.delete()
    return redirect('list_categories')


# Provider Views Their Services
@provider_required
def provider_services(request):
    services = ProviderService.objects.filter(provider=request.user)
    return render(request, 'services/provider_services.html', {'services': services})


# Provider Adds New Service
@provider_required
def add_service(request):
    categories = ServiceCategory.objects.all()

    if request.method == 'POST':
        service_name = request.POST['service_name']
        category_id = request.POST['category']
        price = request.POST['price']
        description = request.POST['description']

        ProviderService.objects.create(
            provider=request.user,
            category_id=category_id,
            service_name=service_name,
            price=price,
            description=description
        )
        return redirect('provider_services')

    return render(request, 'services/add_service.html', {'categories': categories})

@login_required
def view_bookings(request):
    # In real projects, you'd fetch bookings related to this user
    bookings = []  # placeholder for future logic
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

def server_up(request):
    return JsonResponse({"message": "Hello from Django Smart Service!","time": str(datetime.datetime.now())})
