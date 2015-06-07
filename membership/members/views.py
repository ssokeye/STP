from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#All views are mapped to a url
def index(request):
	return HttpResponse("Hello, world You're at the polls index.")

def detail(request, Dept_Name):
    return HttpResponse("You're looking at Department %s." % Dept_Name)