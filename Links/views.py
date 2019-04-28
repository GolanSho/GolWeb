from django.shortcuts import render
from django.http import HttpResponse
from .models import Links


def index(request):
	links = Links.objects.all()
	return render(request, 'index.html', {'links': links})


