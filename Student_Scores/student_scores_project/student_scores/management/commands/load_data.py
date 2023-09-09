
import csv
from django.core.management.base import BaseCommand
from student_scores.models import Student

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def handle(self, *args, **kwargs):
        csv_file = 'C:/Users/Jyoti Ojha/Desktop/student_marks.csv' 
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                Student.objects.create(**row)
