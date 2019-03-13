from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return HttpResponse("I am home")


def index(request):    
    return render(request, 'project/myproject.html')    

def child(request):    
    return render(request, 'project/childpage.html')    

def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)