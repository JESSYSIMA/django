from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('add/', views.add_student, name='add_student'), 
    path('getAll/', views.get_all_students, name='get_all_students'), 
    path('getAllStudentsUniversity/', views.get_all_students_university, name='get_all_students_university'),
    path('findStudentsByUniversity/', views.find_students_by_university, name='find_students_by_university'),
]