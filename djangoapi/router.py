from api.viewsets import *
from api.views import TenantViewSet, SingleUserViewSet, LatestReportViewSet, FilterCaseViewSet, ScoreViewSet, ReportedCaseView, ResolvedCaseView
from rest_framework import routers

router = routers.DefaultRouter()

# reports
router.register('report', ReportViewSet)
router.register('previewReport', PreviewReportViewSet)
router.register('latestReport', LatestReportViewSet, basename='latestReport')

# cases
router.register('case', CaseViewSet)
router.register('filterCases', FilterCaseViewSet, basename='filterCase')

# statistics
router.register('score', ScoreViewSet, basename='score')
router.register('reportedCase', ReportedCaseView, basename='reportedCase')
router.register('resolvedCase', ResolvedCaseView, basename='resolvedCase')

# router.register('unresolvedStats', UnresolvedStatsViewSet)

# users
router.register('users', UserViewSet)
router.register('singleUser', SingleUserViewSet, basename='singleUser')
router.register('tenants', TenantViewSet, basename='tenants')

# news
#router.register('news', NewsViewSet)

