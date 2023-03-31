from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, template_name="home.html")


def about(request):
    return render(request, template_name="about.html")


def experience(request):
    return render(request, template_name="experience.html")


def education(request):
    return render(request, template_name="education.html")


def skills(request):
    return render(request, template_name="skills.html")


def interests(request):
    return render(request, template_name="interests.html")


def awards(request):
    return render(request, template_name="awards.html")


def show_name(request, name):
    return render(request, 'name.html', name)


def students(request):
    # context = {
    #     "infos": [
    #         {
    #             "name": "Nobel",
    #             "age": 23,
    #             "department": "BCA"
    #         },
    #         {
    #             "name": "Mikan",
    #             "age": 19,
    #             "department": "BIM"
    #         },
    #         {
    #             "name": "Ojas",
    #             "age": 16,
    #             "department": "Management"
    #         }
    #     ]
    # }
    # student = Student.objects.all()
    # student = Students.objects.get(id=1)
    context = {
        "info": Student.objects.all(),
    }
    return render(request, "students.html", context)


def index(request):
    return render(request, "index.html")


def staffs(request):
    context = {
        "info": Staff.objects.all(),
    }
    return render(request, "staff.html", context)
