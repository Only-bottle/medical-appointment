from rest_framework.serializers import ModelSerializer

from .models import NonReimbursementDepartment


class NonReimbursementDepartmentSerializer(ModelSerializer):
    class Meta:
        model = NonReimbursementDepartment
        fields = "__all__"
