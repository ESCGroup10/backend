from django.shortcuts import render
from .serializers import UserSerializer, ReportSerializer
from . import models
from rest_framework import mixins, viewsets
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class TenantViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return models.User.objects.filter(Q(type='F&B')|Q(type='Non F&B'))

class SingleUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.User.objects.all()
        email = self.request.query_params.get('email', None)

        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset

class LatestReportViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReportSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.Report.objects
        tenant_id = self.request.query_params.get('tenant_id', None)

        if tenant_id is not None:
            queryset = queryset.filter(tenant_id=tenant_id).order_by('-report_date')[:1]

        return queryset