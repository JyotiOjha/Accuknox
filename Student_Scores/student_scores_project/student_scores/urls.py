
from django.urls import path
from .views import StudentList, calculate_and_visualize_averages



urlpatterns = [
     path('students/', StudentList.as_view(), name='student-list'),
    path('calculate-averages/', calculate_and_visualize_averages, name='calculate-averages'),

]
