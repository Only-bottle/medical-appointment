from django.urls import path

from .views import Doctors, DoctorTreatmentRequests

urlpatterns = [
    path("", Doctors.as_view()),
    path("<int:pk>/treatment_requests", DoctorTreatmentRequests.as_view()),
]
