from rest_framework.serializers import ModelSerializer

from .models import OperatingHour


class OperatingHourSerializer(ModelSerializer):
    class Meta:
        model = OperatingHour
        fields = "__all__"
