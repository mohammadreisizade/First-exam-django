from unittest import result
from django import views
from django.urls import path
from . import views


app_name = 'base'

urlpatterns = [
    path('', views.home ,name="home"),
    path('result/<int:pk>/', views.result, name="result"),
    path('exam/<int:pk>/', views.exam, name="exam"),
    path('addQuestion/', views.addQuestion, name="addQuestion"),
    path('create_question/', views.create_question, name="create_question"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('exam_block/', views.exam ,name="exam_block"),
    path('exams/', views.exams ,name="exams"),
    path('tes/', views.tes ,name="tes"),
    # path('tess/', views.tess ,name="tess"),
    path('create_exam/', views.createExam, name="create_exam"),
    path('add_and_create_questions/', views.add_and_create_questions, name="add_and_create_questions"),
    path('profile/', views.profileUser, name="profile"),
    path('exams_list/', views.exams_list, name="exams_list"),
    path('results_exams/<int:pk>', views.results_exams, name="results_exams"),
]
