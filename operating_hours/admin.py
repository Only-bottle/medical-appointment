from django.contrib import admin

from .models import OperatingHour


@admin.register(OperatingHour)
class OperatingHourAdmin(admin.ModelAdmin):
    list_display = (
        "doctor",
        "day_of_week",
        "open_time",
        "close_time",
        "lunch_start",
        "lunch_end",
        "created_at",
    )
