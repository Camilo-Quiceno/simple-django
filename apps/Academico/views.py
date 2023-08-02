from django.shortcuts import render
from .models import Course

# Create your views here.
def home(request):
    courses_list = Course.objects.all()
    return render(request, "manageCourses.html", {"courses": courses_list})