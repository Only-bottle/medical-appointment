from django.contrib import admin

from .models import NonReimbursementDepartment


@admin.register(NonReimbursementDepartment)
class NonReimbursementDepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )
