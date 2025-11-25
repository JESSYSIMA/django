from rest_framework import serializers
from .models import Student
from university.serializers import UniversitySerializer

class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'address', 'university']
