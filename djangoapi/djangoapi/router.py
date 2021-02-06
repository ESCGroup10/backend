from api.viewsets import ReportViewSet, NewsViewSet, PreviewReportViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('report', ReportViewSet)
router.register('previewReport', PreviewReportViewSet)
router.register('news', NewsViewSet)
