from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager

# Create your models here.

class User(AbstractUser):

    # Additional fields
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30, blank="True")
    location = models.CharField(max_length=200, blank="True")
    institution = models.CharField(max_length=30, blank="True")
    type = models.CharField(max_length=30)


    # Necessary fields for custom user model
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Report(models.Model):

    # basic info
    auditor_id = models.IntegerField(default=0)
    tenant_id = models.IntegerField(default=0)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=100, blank=True)
    outlet_type = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    # report details
    report_notes = models.CharField(max_length=500, blank=True)
    report_date = models.DateTimeField(default=datetime.now)
    report_image = models.CharField(max_length=200, blank=True)

    # resolution details
    resolution_notes = models.CharField(max_length=500, blank=True)
    resolution_date = models.CharField(max_length=100, blank=True)
    resolution_image = models.CharField(max_length=200, blank=True)

    # scores
    staffhygiene_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    housekeeping_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    safety_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    healthierchoice_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    foodhygiene_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)

class Case(models.Model):

    report_id = models.IntegerField()
    question = models.CharField(max_length=200)

    is_resolved = models.BooleanField(null=True)
    non_compliance_type = models.CharField(max_length=100, choices=(('Professional & Staff Hygiene', 'Professional & Staff Hygiene'), ('Housekeeping & General Cleanliness', 'Housekeeping & General Cleanliness'), ('Workplace Safety & Health', 'Workplace Safety & Health'), ('Healthier Choice', 'Healthier Choice'), ('Food Hygiene', 'Food Hygiene')))

    unresolved_photo = models.CharField(max_length=100, blank=True)
    unresolved_comments = models.TextField(blank=True)
    unresolved_date = models.DateTimeField(blank=True)

    resolved_photo = models.CharField(max_length=100, blank=True)
    resolved_comments = models.TextField(blank=True)
    resolved_date = models.DateTimeField(null=True)
