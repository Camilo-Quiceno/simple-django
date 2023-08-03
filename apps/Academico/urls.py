from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registerAction/', views.registerCourse),
    path('deleteCourse/<code>', views.deleteCourse)
]
