from django.urls import path

from .views import OperatingHours, OperatingHourDetail

urlpatterns = [
    path("", OperatingHours.as_view()),
    path("<int:pk>", OperatingHourDetail.as_view()),
]
