from rest_framework.serializers import ModelSerializer, CharField

from .models import TreatmentRequest


class TreatmentRequestSerializer(ModelSerializer):
    patient = CharField(source='patient.name')
    doctor = CharField(source='doctor.name')

    class Meta:
        model = TreatmentRequest
        # fields = "__all__"
        fields = (
            "id",
            "patient",
            "doctor",
            "desired_hours",
            "expired_hours",
            "acceptance",
        )
