from rest_framework import serializers
from CourseApp.models import Course

class  CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','description','rating']