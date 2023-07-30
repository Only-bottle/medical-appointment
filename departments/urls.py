from django.urls import path

from .views import Departments, DepartmentDetail

urlpatterns = [
    path("", Departments.as_view()),
    path("<int:pk>", DepartmentDetail.as_view()),
]
