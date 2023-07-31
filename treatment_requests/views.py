from datetime import datetime, time, timedelta

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)

from .models import TreatmentRequest
from .serializers import TreatmentRequestSerializer
from doctors.models import Doctor


class TreatmentRequests(APIView):
    def get(self, request):
        treatment_requests = TreatmentRequest.objects.all()
        serializer = TreatmentRequestSerializer(
            treatment_requests,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        desired_hours = request.data["desired_hours"]
        datetime_obj = datetime.strptime(desired_hours, '%Y-%m-%d %H:%M:%S')
        date_obj = datetime_obj.date()
        time_part = datetime_obj.strftime('%H:%M:%S')
        day_of_week = datetime_obj.strftime('%A').lower()
        appointment_time = time.fromisoformat(time_part)  # 문자열을 datetime.time 객체로 변환

        serializer = TreatmentRequestSerializer(data=request.data)

        # 의사의 영업 시간을 조회
        doctor = Doctor.objects.get(pk=request.data["doctor"])
        days = doctor.operatinghours.all()
        operating_day = doctor.operatinghours.filter(day_of_week=day_of_week).first()
        if not operating_day:
            desired_hours = "해당 시간은 휴무일 입니다. 다른 날짜를 선택해주세요."

        is_working_day = False
        for day in days:
            if day.day_of_week == day_of_week:
                is_working_day = True
                break
        
        # 영업일이면
        if is_working_day:
            # 의사의 영업 시간과 희망 진료 시간을 비교 만족
            if (day.open_time <= appointment_time < day.lunch_start) or (day.lunch_end < appointment_time <= day.close_time):
                expired_hours = datetime_obj + timedelta(minutes=20)  # 기본적으로 만료시간은 +20분
            else:  # 쉬는 시간에 요청이 들어오는 경우 만료 시간은 다음 영업 시간 + 15분
                # 점심 시간에 들어온 요청
                if day.lunch_start <= appointment_time <= day.lunch_end:
                    next_opening_time = datetime.combine(datetime_obj, day.lunch_end)
                    expired_hours = next_opening_time + timedelta(minutes=15)  # 점심시간 끝나고부터 +15분
                # 휴무나 영업 시간이 종료된 시점
                else:
                    # 다음 영업이 시작되는 날짜 구하기
                    while True:
                        next_day_obj = date_obj + timedelta(days=1)  # 토, 일, 월
                        next_day = next_day_obj.strftime('%A').lower()
                        print(next_day)
                        operating_day = doctor.operatinghours.filter(day_of_week=next_day).first()
                        if not operating_day:
                            date_obj = next_day_obj
                        else:
                            break
                    next_opening_time = datetime.combine(next_day_obj, day.open_time)
                    expired_hours = next_opening_time + timedelta(minutes=15)  # 점심시간 끝나고부터 +15분
                desired_hours = "해당 시간은 영업 시간이 아닙니다. 다른 시간을 선택해주세요."
        else:
            # 다음 영업이 시작되는 날짜 구하기
            while True:
                next_day_obj = date_obj + timedelta(days=1)
                next_day = next_day_obj.strftime('%A').lower()
                operating_day = doctor.operatinghours.filter(day_of_week=next_day).first()
                if not operating_day:
                    date_obj = next_day_obj
                else:
                    break
            next_opening_time = datetime.combine(next_day_obj, day.open_time)
            expired_hours = next_opening_time + timedelta(minutes=15)  # 점심시간 끝나고부터 +15분
            desired_hours = "해당 시간은 휴무일 입니다. 다른 날짜를 선택해주세요."

        if serializer.is_valid():
            treatment_request = serializer.save(
                expired_hours=expired_hours
            )
            return Response(TreatmentRequestSerializer(treatment_request).data)
        else:
            return Response(serializer.errors)


class TreatmentRequestDetail(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass


class TreatmentRequestAccept(APIView):
    def get_object(self, pk):
        pass

    def get(self, request, pk):
        treatment_request = TreatmentRequest.objects.get(pk=pk)
        
        pass

    def delete(self, request, pk):
        pass

    def put(self, request, pk):
        pass
