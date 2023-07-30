from django.db import models

from common.models import CommonModel


class Doctor(CommonModel):

    """Model Definition for Patient"""

    name = models.CharField(max_length=140)
    hospital_name = models.CharField(max_length=140)
    departments = models.ManyToManyField(
        "doctors.Department",
        related_name="doctors",
    )  # 여러 개의 department를 가질 수 있음
    non_reimbursement_subjects = models.ManyToManyField(
        "doctors.NonReimbursementDepartment",
        related_name="doctors",
        blank=True,
    )  # 여러 개의 non_reimbursement_subjects를 가질 수 있음

    def __str__(self) -> str:
        return self.name


class Department(CommonModel):

    """Department Model Definition"""

    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Departments"


class NonReimbursementDepartment(CommonModel):

    """NonReimbursementDepartment Model Definition"""

    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "NonReimbursementDepartments"


class OperatingHour(CommonModel):

    """OperatingHour Model Definition"""

    class DayKindChoices(models.TextChoices):
        MON = ("monday", "Monday")
        TUE = ("tuesday", "Tuesday")
        WED = ("wednesday", "Wednesday")
        THU = ("thursday", "Thursday")
        FRI = ("friday", "Friday")
        SAT = ("saturday", "Saturday")
        SUN = ("sunday", "Sunday")

    day_of_week = models.CharField(max_length=20, choices=DayKindChoices.choices)
    open_time = models.TimeField()
    close_time = models.TimeField()
    lunch_start = models.TimeField()
    lunch_end = models.TimeField()
    doctor = models.ForeignKey(
        "doctors.Doctor",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="operatinghours",
    )

    def __str__(self) -> str:
        return self.day_of_week
    
    class Meta:
        verbose_name_plural = "OperatingHours"