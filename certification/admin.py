from django.contrib import admin
from .models import Certification

# Register your models here.

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "code",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = (
        "is_active",
    )

    ordering = ("-is_active", "-updated_at")