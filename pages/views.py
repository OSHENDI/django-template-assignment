from django.shortcuts import render
import datetime


def index(request):
    profile = {
        "first_name": "osama",
        "last_name": "alhendi",
        "student_id": "120211752",
        "address": "gaza - deir albalah",
        "email": "",
        "major": "IT - software development",
        "dob": datetime.date(2003, 1, 1),
        "description": "I am an IT student at IUG with an interest in web development. Currently learning about the Django framework and how to use it to create web applications.",
        "course": "Advanced Web Programming",
    }
    return render(request, "pages/index.html", context=profile)
