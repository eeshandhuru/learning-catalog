from django.contrib import admin
from .models import VendorProductMapping

# Register your models here.

@admin.register(VendorProductMapping)
class VendorProductMappingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "vendor",
        "product",
        "primary_mapping",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "vendor",
        "primary_mapping",
        "is_active",
    )

    search_fields = (
        "vendor__name",
        "product__name",
    )

    autocomplete_fields = ("vendor", "product")
    
    ordering = ("is_active", "-updated_at",)