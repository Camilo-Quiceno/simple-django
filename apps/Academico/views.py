from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Course

# Create your views here.
def home(request):
    courses_list = Course.objects.all()
    return render(request, "manageCourses.html", {"courses": courses_list})

def registerCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['numCredits']
    
    Course.objects.create(code=code, name=name, credits=credits)
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
    return redirect('/', RequestContext(request))

def deleteCourse(request, code):
    course = Course.objects.get(code=code)
    course.delete()
    return redirect('/', RequestContext(request))