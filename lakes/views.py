from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<p>home view</p>')

def lake_detail(request, id):
	return HttpResponse('<p>lake_detail view with id {}</p>'.format(id))