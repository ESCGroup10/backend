from rest_framework import serializers
from .models import *

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# Preview All Reports
class PreviewReportSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'tenant_id', 'status', 'report_date', 'resolution_date']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

# class CaseStatsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CaseStats
#         fields = '__all__'

class ReportedCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedCase
        fields = ('tenant_id', 'month', 'count')

class ResolvedCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolvedCase
        fields = ('tenant_id','month', 'count')

# class NewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id', 'name', 'company', 'location', 'institution', 'type']

    def save(self, commit=True):

        # Save the provided password in hashed format
        user = User(
            email = self.validated_data['email'],     
            name = self.validated_data['name'],
            company = self.validated_data['company'],
            location = self.validated_data['location'],
            institution = self.validated_data['institution'],
            type = self.validated_data['type']
        ) 
        user.set_password(self.validated_data["password"])
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user