from rest_framework import serializers
from .models import Report, News

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# Preview All Reports
class PreviewReportSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'stall', 'status', 'report_date', 'resolution_date']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'