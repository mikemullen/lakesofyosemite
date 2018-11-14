from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Lake

def home(request):
	return render(request, 'home.html')

def lake_detail(request, slug):
	try:
		lake = Lake.objects.get(slug=slug)
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_detail.html', {'lake': lake})

def lakes_lists(request):
	lakes = Lake.objects.all()
	return render(request, 'lakes_lists.html', {'lakes': lakes})