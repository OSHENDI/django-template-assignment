from django.shortcuts import render
from .models import Student


def index(request):
    student = Student.objects.first()
    return render(request, "pages/index.html", {"student": student})
