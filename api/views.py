from django.shortcuts import render
from .serializers import UserSerializer
from . import models
from rest_framework import mixins, viewsets
from django.db.models import Q


# Create your views here.
class TenantViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return models.User.objects.filter(Q(type='F&B')|Q(type='Non F&B'))