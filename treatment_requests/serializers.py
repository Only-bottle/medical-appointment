from rest_framework.serializers import ModelSerializer

from .models import TreatmentRequest


class TreatmentRequestSerializer(ModelSerializer):
    class Meta:
        model = TreatmentRequest
        fields = "__all__"
