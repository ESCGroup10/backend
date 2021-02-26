from api.viewsets import *
from api.views import TenantViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('report', ReportViewSet)
router.register('previewReport', PreviewReportViewSet)
router.register('news', NewsViewSet)
router.register('users', UserViewSet)

router.register('tenants', TenantViewSet, basename='tenants')
router.register('auth', AuthViewSet)
