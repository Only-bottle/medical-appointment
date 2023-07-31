"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/doctors/", include("doctors.urls")),
    path("api/v1/departments/", include("departments.urls")),
    path("api/v1/non_reimbursement_subjects/", include("non_reimbursement_subjects.urls")),
    path("api/v1/patients/", include("patients.urls")),
    path("api/v1/operating_hours/", include("operating_hours.urls")),
    path("api/v1/treatment_requests/", include("treatment_requests.urls")),
]
