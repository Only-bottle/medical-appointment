from django.db import models

from common.models import CommonModel


class Doctor(CommonModel):

    """Model Definition for Patient"""

    name = models.CharField(max_length=140)
    hospital_name = models.CharField(max_length=140)
    departments = models.ManyToManyField(
        "departments.Department",
        related_name="doctors",
    )  # 여러 개의 department를 가질 수 있음
    non_reimbursement_subjects = models.ManyToManyField(
        "non_reimbursement_subjects.NonReimbursementDepartment",
        related_name="doctors",
        blank=True,
    )  # 여러 개의 non_reimbursement_subjects를 가질 수 있음

    def __str__(self) -> str:
        return self.name
