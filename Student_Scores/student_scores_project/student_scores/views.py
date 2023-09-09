
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

import matplotlib.pyplot as plt
from django.http import HttpResponse
from io import BytesIO

def calculate_and_visualize_averages(request):
    students = Student.objects.all()
    
    student_ids = [student.Student_ID for student in students]
    average_scores = [(student.Test_1 + student.Test_2 + student.Test_3 + student.Test_4 + student.Test_5 + student.Test_6 + student.Test_7 + student.Test_8 + student.Test_9 + student.Test_10 + student.Test_11 + student.Test_12) / 12 for student in students]
    
   
    plt.bar(student_ids, average_scores)
    plt.xlabel('Student ID')
    plt.ylabel('Average Score')
    plt.title('Average Scores of Students')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    buffer.seek(0)
    
    response = HttpResponse(buffer, content_type='image/png')
    return response
