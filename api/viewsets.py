from rest_framework import viewsets
from . import models
from . import serializers

from django.db.models import Count
from django.db.models.functions import ExtractMonth

class ReportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

class PreviewReportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.PreviewReportSeriazlier

class CaseViewSet(viewsets.ModelViewSet):
    queryset = models.Case.objects.all()
    serializer_class = serializers.CaseSerializer

# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = models.News.objects.all()
#     serializer_class = serializers.NewsSerializer

# class UnresolvedStatsViewSet(viewsets.ModelViewSet):
#     queryset = models.CaseStats.objects.annotate(month=ExtractMonth('unresolved_date')).values('month', 'reported').annotate(count=Count('id')).values('month').order_by('month')
#     serializer_class = serializers.CaseStatsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

# class AuthViewSet(viewsets.ModelViewSet):
#     queryset = models.Auth.objects.all()
#     serializer_class = serializers.AuthSerializer
