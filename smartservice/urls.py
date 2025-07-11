from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),

    # Dummy dashboards
    path('user/home/', lambda r: HttpResponse("<h1>User Dashboard</h1>")),
    path('provider/home/', lambda r: HttpResponse("<h1>Provider Dashboard</h1>")),
]
