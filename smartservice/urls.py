from django.urls import path, include
from accounts.views import ping_view

urlpatterns = [
    path('', include('accounts.urls')),
        path('ping/', ping_view),  # URL: https://loan-app-wjbq.onrender.com/api/server/start


]
