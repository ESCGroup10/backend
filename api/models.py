from django.db import models
from datetime import datetime

# Create your models here.

class Report(models.Model):

    # basic info
    auditor_id = models.IntegerField(default=0)
    tenant_id = models.IntegerField(default=0)
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
    staffhygiene_score = models.IntegerField(default=0)
    housekeeping_score = models.IntegerField(default=0)
    safety_score = models.IntegerField(default=0)
    healthierchoice_score = models.IntegerField(default=0)
    foodhygiene_score = models.IntegerField(default=0)

# class News(models.Model):
#     auditor_id = models.CharField(max_length=30)
#     title = models.CharField(max_length=100)
#     details = models.TextField()
#     news_date = models.DateTimeField(default=datetime.now)

class User(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30, blank="True")
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=200, blank="True")
    institution = models.CharField(max_length=30, blank="True")
    type = models.CharField(max_length=30)

# class Auth(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)