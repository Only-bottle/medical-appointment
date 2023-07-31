from django.contrib import admin

from .models import TreatmentRequest


@admin.register(TreatmentRequest)
class TreatmentRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "doctor",
        "desired_hours",
        "expired_hours",
        "acceptance",
    )
