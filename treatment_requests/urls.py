from django.urls import path

from .views import TreatmentRequests, TreatmentRequestDetail, TreatmentRequestAccept

urlpatterns = [
    path("", TreatmentRequests.as_view()),
    path("<int:pk>", TreatmentRequestDetail.as_view()),
    path("<int:pk>/accept", TreatmentRequestAccept.as_view()),
]
