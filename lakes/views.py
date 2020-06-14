from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Lake

def home(request):
	return render(request, 'home.html')

def lake_detail(request, slug):
	lakes = Lake.objects.order_by('-name')
	try:
		lake = Lake.objects.get(slug=slug)
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_detail.html', {'lake': lake})

def lake_images(request, slug):
	try:
		lake = Lake.objects.get(slug=slug)
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_images.html', {'lake': lake})

def lakes_lists(request):
	lakes = Lake.objects.order_by('name')
	lakesTopTenByElevation = Lake.objects.order_by('-elevation')[0:10]
	lakesTopTenByArea = Lake.objects.order_by('-size')[0:10]

	return render(request, 'lakes_lists.html', {'lakes': lakes,
												'lakesTopTenByElevation': lakesTopTenByElevation,
												'lakesTopTenByArea': lakesTopTenByArea})
	