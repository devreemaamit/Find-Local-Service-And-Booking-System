from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_paths = [
            reverse('login'),
            reverse('signup'),
            '/admin/login/',  # allow Django admin login
            '/static/',       # allow static files
            '/api/serverup'
        ]

    def __call__(self, request):
        path = request.path

        if not request.user.is_authenticated and not any(path.startswith(p) for p in self.allowed_paths):
            return redirect('login')

        return self.get_response(request)
