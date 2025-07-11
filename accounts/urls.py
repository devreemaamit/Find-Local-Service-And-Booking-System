from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/home/', views.admin_home, name='admin_home'),
    path('users/home/', views.user_home, name='user_home'),
    path('provider/home/', views.provider_home, name='provider_home'),

    path('', views.dashboard_redirect, name='dashboard'), 
]
