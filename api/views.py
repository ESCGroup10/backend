from django.shortcuts import render
from .serializers import UserSerializer, ReportSerializer, CaseSerializer, ReportedCaseSerializer, ResolvedCaseSerializer
from . import models
from rest_framework import mixins, viewsets
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import F

from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.

class TenantViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return models.User.objects.filter(Q(type='F&B') | Q(type='Non F&B'))


class SingleUserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.User.objects.all()
        email = self.request.query_params.get('email', None)

        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset


class FilterCaseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CaseSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.Case.objects.all()
        
        report_id = self.request.query_params.get('report_id', None)
        # case_id = self.request.query_params.get('id', None)
        is_resolved = self.request.query_params.get('is_resolved', None)

        if report_id is not None:
            queryset = queryset.filter(report_id=report_id)
        # if case_id is not None:
        #     queryset = queryset.filter(id=case_id)
        if is_resolved is not None:
            queryset = queryset.filter(is_resolved=is_resolved)

        return queryset


class LatestReportViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReportSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.Report.objects
        tenant_id = self.request.query_params.get('tenant_id', None)

        if tenant_id is not None:
            queryset = queryset.filter(
                tenant_id=tenant_id).order_by('-report_date')[:1]

        return queryset


class ScoreViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ReportSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = models.Report.objects
        tenant_id = self.request.query_params.get('tenant_id', None)

        if tenant_id is not None:
            queryset = queryset.filter(tenant_id=tenant_id)

        return queryset


class ReportedCaseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Case.objects.annotate(month=TruncMonth('unresolved_date')).values('tenant_id', 'month').annotate(count=Count('id')).values('tenant_id', 'month', 'count').order_by('-month')
    serializer_class = ReportedCaseSerializer

    def get_queryset(self):
        queryset = models.Case.objects.annotate(month=TruncMonth('unresolved_date')).values('tenant_id', 'month').annotate(count=Count('id')).values('tenant_id', 'month', 'count').order_by('-month')
        tenant_id = self.request.query_params.get('tenant_id', None)

        if tenant_id is not None:
            queryset = queryset.filter(tenant_id=tenant_id)

        return queryset
    


class ResolvedCaseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Case.objects.annotate(month=TruncMonth('resolved_date')).values('tenant_id','month').annotate(count=Count('id')).values('tenant_id','month', 'count').order_by('-month')
    serializer_class = ResolvedCaseSerializer

    def get_queryset(self):
        queryset = models.Case.objects.annotate(month=TruncMonth('unresolved_date')).values('tenant_id', 'month').annotate(count=Count('id')).values('tenant_id', 'month', 'count').order_by('-month')
        tenant_id = self.request.query_params.get('tenant_id', None)

        if tenant_id is not None:
            queryset = queryset.filter(tenant_id=tenant_id)

        return queryset