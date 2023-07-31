from django.db import models

from common.models import CommonModel


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
    lunch_start = models.TimeField(blank=True, null=True)
    lunch_end = models.TimeField(blank=True, null=True)
    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE,
        related_name="operatinghours",
    )

    def __str__(self) -> str:
        return self.day_of_week

    class Meta:
        verbose_name_plural = "OperatingHours"
