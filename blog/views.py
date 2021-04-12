from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse

def details(request, pkid):
    blog = Blog.objects.filter(pk=pkid)
    context = {
        'blog': blog
    }
    return HttpResponse(blog.title)


def home(request):
    return HttpResponse('Home page')

def contact(request):
    return HttpResponse('contact page')