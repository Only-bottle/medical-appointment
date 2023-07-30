from django.urls import path

from .views import Doctors, DoctorDetail

urlpatterns = [
    path("", Doctors.as_view()),
    path("<int:pk>", DoctorDetail.as_view()),
]
