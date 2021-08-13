from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(req):
    return HttpResponse('hai how are you')
def hello(req):
    return HttpResponse('<h1><marquee>malli is mad</marquee></h1>')    
