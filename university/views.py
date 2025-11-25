from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import University
from .serializers import UniversitySerializer 
 
@api_view(['POST']) 
def add_university(request): 
    serializer = UniversitySerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response({"message": "New University is added"}) 
    return Response(serializer.errors, status=400) 
 