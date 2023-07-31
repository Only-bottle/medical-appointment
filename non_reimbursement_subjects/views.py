from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import NonReimbursementDepartment
from .serializers import NonReimbursementDepartmentSerializer


class NonReimbursementDepartments(APIView):
    def get(self, request):
        non_reimbursement_departments = NonReimbursementDepartment.objects.all()
        serializer = NonReimbursementDepartmentSerializer(
            non_reimbursement_departments,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        pass


class NonReimbursementDepartmentDetail(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass
