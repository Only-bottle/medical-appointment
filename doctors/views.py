from datetime import datetime, time

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from treatment_requests.models import TreatmentRequest
from treatment_requests.serializers import TreatmentRequestSerializer

from .models import Doctor
from .serializers import DoctorSerializer
from operating_hours.models import OperatingHour


class Doctors(APIView):
    def get(self, request):
        # search_name = request.query_params.get('name', '')
        # print(search_name)
        # doctors = Doctor.objects.filter(name__icontains=search_name)
        # serializer = DoctorSerializer(
        #     doctors,
        #     many=True,
        # )
        # return Response(serializer.data)
        search_date = request.query_params.get("date")
        search_time = request.query_params.get("time")

        print(search_date)

        # Convert date and time strings to Python datetime and time objects
        search_datetime = datetime.strptime(search_date, "%Y-%m-%d").date() if search_date else None
        search_time = datetime.strptime(search_time, "%H:%M").time() if search_time else None

        print(search_datetime, search_time)

        # Find operating hours for the given date and time
        operating_hours = OperatingHour.objects.filter(
            day_of_week=search_datetime.strftime("%a").upper(),
            open_time__lte=search_time,
            close_time__gt=search_time,
        ).values_list("hospital_id", flat=True)

        print(operating_hours)

        # Get the doctors associated with the hospitals having operating hours
        doctors = Doctor.objects.filter(hospital__id__in=operating_hours)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class DoctorTreatmentRequests(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        treatment_requests = TreatmentRequest.objects.filter(
            doctor=pk, acceptance=False
        )
        serializer = TreatmentRequestSerializer(
            treatment_requests,
            many=True,
        )
        return Response(serializer.data)

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass


class DoctorTreatmentRequestDetail(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass
