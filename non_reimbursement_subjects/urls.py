from django.urls import path

from .views import NonReimbursementDepartments, NonReimbursementDepartmentDetail

urlpatterns = [
    path("", NonReimbursementDepartments.as_view()),
    path("<int:pk>", NonReimbursementDepartmentDetail.as_view()),
]
