from django.urls import path

from .views import Patients, PatientDetail

urlpatterns = [
    path("", Patients.as_view()),
    path("<int:pk>", PatientDetail.as_view()),
]
