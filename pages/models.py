from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()
    salary = models.PositiveIntegerField()
    photo = models.FileField(upload_to='photos/')

    def __str__(self):
        return self.full_name
