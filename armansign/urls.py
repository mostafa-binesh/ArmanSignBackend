"""
URL configuration for armansign project.

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
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from accounts.views import OperatorFilterListView, UserGroupsoListView, UserInfoListView, UserViewSet, \
    OperatorAndSupervisorFilterListView, SignupView
from rest_framework.routers import DefaultRouter
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
# router.register(r'parts', partsViews.PartViewSet, basename='part')
# router.register(r'clients', ClientViewSet, basename='client')
# router.register(r'orders', OrderViewSet, basename='client')
# router.register(r'reports', ReportViewSet, basename='report')
# router.register(r'machines', MachineViewSet, basename='machine')
router.register(r'users', UserViewSet, basename='users')
# router.register(r'projects', ProjectViewSet, basename='project')


urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/operators/filterData', OperatorFilterListView.as_view(), name='operator-filter-list'),
    path('api/operators-and-supervisors', OperatorAndSupervisorFilterListView.as_view(), name='operator-filter-list'),
    # path('api/reports/export', ReportExportView.as_view(), name='export-reports'),

    # jwt token routes
    path('api/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/signin/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/user-info/', UserInfoListView.as_view(), name='user_info'),
    path('api/user-groups/', UserGroupsoListView.as_view(), name='user_groups'),
]
