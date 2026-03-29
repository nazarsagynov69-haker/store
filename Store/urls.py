from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import JobViewSet
# from .views import ResumeViewSet
# from .views import ApplicationViewSet
#
router = DefaultRouter()
# router.register(r'jobs', JobViewSet)
# router.register(r'resumes', ResumeViewSet)
# router.register(r'applications', ApplicationViewSet)
#
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Job Platform API",
        default_version='v1',
        description="API для поиска работы",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger')),
]