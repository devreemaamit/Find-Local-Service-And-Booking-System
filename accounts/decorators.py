from django.http import HttpResponseForbidden

def provider_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'provider':
            return HttpResponseForbidden("Only providers can access this page.")
        return view_func(request, *args, **kwargs)
    return wrapper
