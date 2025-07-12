from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            if user.role == 'provider':
                return redirect('provider_home')
            elif user.role == 'user':
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

def ping_view():
    return JsonResponse({'status': 'ok'})

