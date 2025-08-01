from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from accounts.models import CustomUser
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import EditProfileForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user.role == 'provider':
                messages.info(request, "Your account has been created and is pending admin approval.")
                return redirect('login')  # Redirect to login, no dashboard access

            login(request, user)  # only login user if not provider

            if user.role == 'user':
                return redirect('user_home')
            else:
                return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Check provider approval
            if user.role == 'provider' and not user.is_approved:
                messages.error(request, "Your account is not approved yet. Please wait for admin approval.")
                return render(request, 'login.html', {'form': form})

            login(request, user)

            if user.is_superuser:
                return redirect('admin_home')
            elif user.role == 'user':
                return redirect('user_home')
            elif user.role == 'provider':
                return redirect('provider_home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def manage_users(request):
    users = CustomUser.objects.filter(is_active=True)
    return render(request, 'admin/manage_users.html', {'users': users})

@login_required
def manage_providers(request):
    if not request.user.is_superuser:
        return redirect('login')
    providers = CustomUser.objects.filter(role='provider', is_active=True)
    return render(request, 'admin/manage_providers.html', {'providers': providers})

@login_required
def approve_provider(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, role='provider')
    if request.method == 'POST':
        user.is_approved = True
        user.save()
    return redirect(reverse('manage_users'))

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST' and request.user.id != user.id:
        user.is_active = False
        user.save()
        messages.success(request, "User soft deleted successfully.")
    return redirect('manage_users')

# Admin Dashboard View
@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return redirect('login')
    return render(request, 'admin/home.html')

# User Dashboard View
@login_required
def user_home(request):
    if request.user.role != 'user':
        return redirect('login')
    return render(request, 'users/home.html')


# Provider Dashboard View
@login_required
def provider_home(request):
    if request.user.role != 'provider':
        return redirect('login')
    return render(request, 'services/home.html')

@login_required
def dashboard_redirect(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.role == 'user':
        return redirect('user_home')
    elif request.user.role == 'provider':
        return redirect('provider_home')
    else:
        return redirect('login')  # fallback


def logout_view(request):
    logout(request)
    return redirect('login')

def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')

            if hasattr(user, 'role') and user.role == 'provider':
                redirect_url = reverse('provider_home')
            else:
                redirect_url = reverse('user_home')

            return render(request, 'accounts/edit_profile.html', {
                'form': form,
                'redirect_url': redirect_url
            })
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })