from django.shortcuts import render


def index(request):
    profile = {
        'full_name': 'Osama Alhendi',
        'student_id': '120211752',
        'email': 'os@iugaza.edu.ps',
        'major': 'IT - Software Development',
        'description': 'I am an IT student at IUG with an interest in web development. Currently learning about the Django framework and how to use it to create web applications.',
        'course': 'Advanced Web Programming',
    }
    return render(request, 'pages/index.html', context=profile)
