
from django.db import models

class Student(models.Model):
    Student_ID = models.IntegerField(primary_key=True)
    Test_1 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_2 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_3 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_4 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_5 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_6 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_7 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_8 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_9 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_10 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_11 = models.DecimalField(max_digits=5, decimal_places=2)
    Test_12 = models.DecimalField(max_digits=5, decimal_places=2)
