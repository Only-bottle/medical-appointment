from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer


class Patients(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(
            patients,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        pass


class PatientDetail(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass
