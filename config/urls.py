"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from rest_framework.routers import DefaultRouter

from assessments.api.viewsets import AssessmentCreateView
from job.api.viewsets import (
    CategoryViewSet,
    JobRetrieveAPIView,
    JobCreateAPIView,
    JobListAPIView
)

from authentication.api.viewsets import CreateUserView, ChangePasswordAPIView, WhoamiAPIView
from authentication.views import PasswordResetView
from service.api.viewsets import ServiceCreateView, ServiceListView
from tasker.api.viewsets import TaskerServiceActionView

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='period')

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # auth
    path('api/sessions/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/sessions/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('api/reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('reset-password-confirm/', PasswordResetView.as_view(), name='password_reset_confirm_form'),

    # tasker
    path('api/tasker/services/action/', TaskerServiceActionView.as_view(), name='tasker-service-action'),

    # assesments
    path('api/assessments/', AssessmentCreateView.as_view(), name='assessment-create'),
    
    # users
    path('api/users/', CreateUserView.as_view(), name='create_user'),
    path('api/whoami/', WhoamiAPIView.as_view(), name='whoami'),

    # service
    path('api/services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('api/jobs/<int:job_id>/services/', ServiceListView.as_view(), name='job-services'),


    # jobs
    path('api/jobs/create/', JobCreateAPIView.as_view(), name='create_job'),
    path('api/jobs/', JobListAPIView.as_view(), name='list_job'),
    path('api/jobs/<int:pk>/', JobRetrieveAPIView.as_view(), name='retrieve_job'),
    
    # drf-spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # include the router URLs
    path('api/', include(router.urls)),
]
