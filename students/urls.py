from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('allStudents/', views.allStudents, name='allStudents'),
    path('update_student/<int:id>/', views.update_students, name='update_student'),
    path('delete_student/<int:id>/', views.delete_students, name='delete_student'),


]
