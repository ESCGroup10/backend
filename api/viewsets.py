from rest_framework import viewsets
from . import models
from . import serializers

class ReportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

class PreviewReportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.PreviewReportSeriazlier

class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class AuthViewSet(viewsets.ModelViewSet):
    queryset = models.Auth.objects.all()
    serializer_class = serializers.AuthSerializer
