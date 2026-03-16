from django.contrib import admin
from .models import CourseCertificationMapping

# Register your models here.

@admin.register(CourseCertificationMapping)
class CourseCertificationMappingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "course",
        "certification",
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
        "course__name",
        "certification__name",
    )

    autocomplete_fields = ("course", "certification")
    
    ordering = ("-is_active", "-updated_at")