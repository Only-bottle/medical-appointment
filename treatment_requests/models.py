from django.db import models

from common.models import CommonModel


class TreatmentRequest(CommonModel):
    """Model Definition for TreatmentRequests"""

    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE,
        related_name="treatment_requests",
    )  # 환자
    doctor = models.ForeignKey(
        "doctors.Doctor",
        on_delete=models.CASCADE,
        related_name="treatment_requests",
    )  # 의사
    desired_hours = models.DateTimeField()  # 진료 희망 날짜시간
    expired_hours = models.DateTimeField()  # 진료요청 만료 날짜시간
    acceptance = models.BooleanField(default=False)  # 진료 수락 여부
