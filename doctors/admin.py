from django.contrib import admin

from .models import Doctor, Department, NonReimbursementDepartment, OperatingHour


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hospital_name",
        "get_departments",
        "get_non_reimbursement_subject",
        "created_at",
    )

    @admin.display(description='departments')
    def get_departments(self, obj):
        return [department.name for department in obj.departments.all()]

    @admin.display(description='non_reimbursement_subjects')
    def get_non_reimbursement_subject(self, obj):
        return [non_reimbursement_subject.name for non_reimbursement_subject in obj.non_reimbursement_subjects.all()]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )


@admin.register(NonReimbursementDepartment)
class NonReimbursementDepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )


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
