from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Lake

def home(request):
	return render(request, 'home.html')

def lake_detail(request, id):
	try:
		lake = Lake.objects.get(id=id)
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_detail.html', {'lake': lake})