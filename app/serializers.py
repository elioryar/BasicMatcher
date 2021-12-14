from django.db.models import fields
from .models import Job, Candidate
from rest_framework import serializers

#this file responsble to convert model instance to Object datatype.

class JobSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=500)
    skills = serializers.ListField(child = serializers.CharField())
    class Meta:
        model = Job
        fields = ['id', 'title', 'skills']

        
class CandidateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=500)
    skills = serializers.ListField(child = serializers.CharField())
    class Meta:
        model = Candidate
        fields = ['id', 'title', 'skills']