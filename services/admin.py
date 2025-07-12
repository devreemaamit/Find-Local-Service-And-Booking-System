from django.contrib import admin
from .models import ServiceCategory, ProviderService

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 20

@admin.register(ProviderService)
class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'provider', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('service_name', 'provider__username')
    list_per_page = 20
