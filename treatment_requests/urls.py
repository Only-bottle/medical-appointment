from django.urls import path

from .views import TreatmentRequests, TreatmentRequestDetail

urlpatterns = [
    path("", TreatmentRequests.as_view()),
    path("<int:pk>", TreatmentRequestDetail.as_view()),
]
