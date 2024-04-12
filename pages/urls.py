from django.urls import path
from  . import views
from .views import home_page_view

urlpatterns = [
    path("test", home_page_view, name="home"),
    path('student/signup_student', views.signup_student, name='signup_student'),
    path('student/signup_student_output', views.signup_student_output, name='signup_student_output2'),
]