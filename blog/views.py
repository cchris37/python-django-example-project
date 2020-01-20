from django.shortcuts import render
from django.http import HttpResponse

def name():
	return "Christian's"

def putin_h1(string):
	return "<h1>{}</h1>".format(string)

def home (request):
	return HttpResponse (putin_h1("{} Blog Home".format(name())))

def about (recuest):
	return HttpResponse (putin_h1("{} Blog About".format(name())))


# Create your views here.
