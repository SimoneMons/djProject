from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import student

def home_page_view(request):
    return render(request, 'home.html', locals())

def signup_student(request):
    return render(request,'signup_student.html',{'msg':'Student Signup'})


def signup_student_output(request):
    en=student(name=request.POST.get('name'),cl=request.POST.get('class'),
     mark=request.POST.get('mark'),gender=request.POST.get('gender'))
    en.save()

    mydata = student.objects.all().values()
    template = loader.get_template('show_students.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
