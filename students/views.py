from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Student, University
from .serializers import StudentSerializer 
 
@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        university_id = request.data.get("university")

        # Vérifier si l'université existe
        if not University.objects.filter(id=university_id).exists():
            return Response({"error": "University not found"}, status=404)

        # Récupérer l'objet université
        univ = University.objects.get(id=university_id)

        # Sauvegarder l'étudiant
        serializer.save(university=univ)
        return Response({"message": "New student is added"})
    
    return Response(serializer.errors, status=400)

 
@api_view(['GET']) 
def get_all_students(request): 
    students = Student.objects.all() 
    serializer = StudentSerializer(students, many=True) 
    return Response(serializer.data)
@api_view(['GET'])
def get_all_students_university(request):
    data = Student.objects.select_related('university').values('name', 'university__name')
    return Response(list(data))
@api_view(['GET'])
def find_students_by_university(request):
    univ_name = request.GET.get('univName')
    students = Student.objects.filter(university__name=univ_name).values('name', 'university__name')
    return Response(list(students))
