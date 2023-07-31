from django.urls import path

from .views import Doctors, DoctorTreatmentRequests, DoctorTreatmentRequestDetail

urlpatterns = [
    path("", Doctors.as_view()),
    path("<int:pk>/treatment_requests", DoctorTreatmentRequests.as_view()),
    path("<int:pk>/treatment_requests/<int:request_pk>/accept", DoctorTreatmentRequestDetail.as_view()),
]
