from django.shortcuts import render
from .models import Courses, Year, Branch, Document_type, Documents, Wifi
from django.urls import reverse
from django.http import HttpResponseRedirect
import os
import mimetypes
from django.http.response import HttpResponse
from django.conf import settings
from django.urls import reverse

def home(request):
    # return HttpResponse('Hi')
    years = Year.objects.all()
    context = {
        "years" : years
    }
    return render(request, 'academics/home.html', context)

def branch(request, year):
    branches = Branch.objects.all()
    print(branches)
    context = {
        "year_number" : year,
        "branches" : branches
    }
    return render(request, 'academics/branch.html', context)

def course(request, year, branch_id):
    print("here is the branch id", branch_id)
    print(type(branch_id))
    branch_ob = Branch.objects.filter(id = branch_id)
    print(branch_ob)
    
    try:
        courses = Courses.objects.filter(branch = branch_ob[0])
    except Branch.DoesNotExist:
        print("Course dont exist")

    print(courses)

    context = {
        "courses" : courses
    }

    return render(request, 'academics/course.html', context)

def documents(request, course_id):
    document_type = Document_type.objects.all()
    context = {
        "types" : document_type,
        "course_id" : course_id
    }
    return render(request, 'academics/documents.html', context)

def show_documents(request, course_id, type_id):
    document_type = Document_type.objects.filter(id = type_id)
    course = Courses.objects.filter(id = course_id)
    print(document_type[0])
    print(course)
    documents = Documents.objects.filter(course = course[0], type = document_type[0])
    context = {
        "documents" : documents,
        "type" : document_type[0]
    }
    return render(request, 'academics/show_documents.html', context)

def wifi(request):
    wifis = Wifi.objects.all()
    context = {
        "wifis" : wifis
    }
    return render(request, 'academics/wifi.html', context)

def gpa(request):
    years = Year.objects.all()
    branches = Branch.objects.all()
    print(years)
    print(branches)
    context = {
        "years" : years,
        "branches" : branches
    }
    if request.method == "POST":
        year_id = request.POST.get('year_id')
        branch_id = request.POST.get('branch_id')
        print(type(year_id))
        print("YEAR_ID", year_id, " ", branch_id)
        return HttpResponseRedirect(reverse("gpa_calc", args=(year_id, branch_id)))
    return render(request, 'academics/gpa_calculator.html', context)

def gpa_calc(request, year_id, branch_id):
    print("REACHED GPA CALC")
    print(year_id, branch_id)
    branch_ob = Branch.objects.filter(id = branch_id)
    year_ob = Year.objects.filter(id = year_id)
    courses = Courses.objects.filter(branch = branch_ob[0], year = year_ob[0]).all()
    print(courses)
    context = {
        "courses" : courses
    }
    return render(request, 'academics/show_gpa_calculator.html', context)