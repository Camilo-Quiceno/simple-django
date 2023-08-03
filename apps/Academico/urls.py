from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerAction/', views.registerCourse),
    path('editCourse/<code>', views.editCourse),
    path('courseEdited/', views.courseEdited),
    path('deleteCourse/<code>', views.deleteCourse)
]
