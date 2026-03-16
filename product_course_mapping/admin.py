from django.contrib import admin
from .models import ProductCourseMapping

# Register your models here.

@admin.register(ProductCourseMapping)
class ProductCourseMappingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "product",
        "course",
        "primary_mapping",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "primary_mapping",
        "is_active",
    )

    search_fields = (
        "product__name",
        "course__name",
    )

    autocomplete_fields = ("product", "course")
    
    ordering = ("-is_active", "-updated_at")