from django.urls import path, include
from accounts.views import ping_view
from services.views import server_up

urlpatterns = [
    path('', include('accounts.urls')),
    path('services/', include('services.urls')),
    path('api/serverup', server_up),  # Make sure this line exists

]
