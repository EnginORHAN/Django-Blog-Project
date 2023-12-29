from django.shortcuts import render
from appMy.models import *
# Create your views here.

def indexPage(request):
    blog_list = Blog.objects.all()
    context={
        "blog_list":blog_list,
    }
    return render(request,"index.html",context)

def categoryPage(request):
    blog_list = Blog.objects.all()
    context={
        "blog_list":blog_list,
    }
    return render(request,"category.html",context)

def aboutPage(request):
    context={}
    return render(request,"about.html",context)

def contactPage(request):
    context={}
    return render(request,"contact.html",context)