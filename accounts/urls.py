from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/home/', views.admin_home, name='admin_home'),
    path('users/home/', views.user_home, name='user_home'),
    path('provider/home/', views.provider_home, name='provider_home'),
    path('admin/users/', views.manage_users, name='manage_users'),
    path('admin/providers/', views.manage_providers, name='manage_providers'),
    path('admin/approve-provider/<int:user_id>/', views.approve_provider, name='approve_provider'),
    path('admin/delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
    path('', views.dashboard_redirect, name='dashboard'),
    path("ping/", lambda request: HttpResponse("pong")),

]
