from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
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
            if user.role == 'user':
                return redirect('/user/home/')
            elif user.role == 'provider':
                return redirect('/provider/home/')
            elif user.is_superuser:
                return redirect('/admin/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
