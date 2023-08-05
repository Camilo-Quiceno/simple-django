from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Course
from django.contrib import messages

# Create your views here.
def home(request):
    courses_list = Course.objects.all()
    messages.success(request, "Courses Listed!")
    return render(request, "manageCourses.html", {"courses": courses_list})

def registerCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['numCredits']
    
    Course.objects.create(code=code, name=name, credits=credits)
    messages.success(request, "Courses Registered")
    return redirect('/', RequestContext(request))

def editCourse(request, code):
    course = Course.objects.get(code=code)
    return render(request, "editCourse.html", {"course": course})

def courseEdited(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['numCredits']
    
    course = Course.objects.get(code=code)
    course.name = name
    course.credits = credits
    course.save()
    messages.success(request, "Course Edited")
    return redirect('/', RequestContext(request))

def deleteCourse(request, code):
    course = Course.objects.get(code=code)
    course.delete()
    messages.success(request, "Courses Deleted")
    return redirect('/', RequestContext(request))