from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Lake

def home(request):
	lakes = Lake.objects.order_by('name')
	photographedlakes = 0
	tophotographlakes = 0
	for lake in lakes:
		if lake.image:
			photographedlakes = photographedlakes + 1
		else:
			tophotographlakes = tophotographlakes + 1


	return render(request, 'home.html', {'photographedlakes': photographedlakes,
										 'tophotographlakes': tophotographlakes})

def lake_detail(request, slug):
	lakes = Lake.objects.order_by('name')
	total = lakes.count()

	try:
		lake = lakes.get(slug=slug)
		index = lakes.filter(name__lt = lake.name).count()
		if index == 0:
			nextlake = lakes[index +1]
			prevlake = lakes[total -1]
		elif index == total -1:
			nextlake = lakes[0]
			prevlake = lakes[index -1]
		else:
			nextlake = lakes[index +1]
			prevlake = lakes[index -1]
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_detail.html', {'lake': lake,
												'nextlake': nextlake,
												'prevlake': prevlake,
												'index': index})

def lake_images(request, slug):
	pholakes = Lake.objects.filter(image__contains='.jpg').order_by('name')
	total = pholakes.count()
	try:
		lake = Lake.objects.get(slug=slug)
		index = pholakes.filter(name__lt = lake.name).count()
		if index == 0:
			nextlake = pholakes[index +1]
			prevlake = pholakes[total -1]
		elif index == total -1:
			nextlake = pholakes[0]
			prevlake = pholakes[index -1]
		else:
			nextlake = pholakes[index +1]
			prevlake = pholakes[index -1]
	except Lake.DoesNotExist:
		raise Http404('Lake not found')
	return render(request, 'lake_images.html', {'lake': lake,
												'nextlake': nextlake,
												'prevlake': prevlake,
												'index': index})

def lakes_lists(request):
	lakes = Lake.objects.order_by('name')
	lakesTopTenByElevation = Lake.objects.order_by('-elevation')[0:10]
	lakesTopTenByArea = Lake.objects.order_by('-size')[0:10]

	return render(request, 'lakes_lists.html', {'lakes': lakes,
												'lakesTopTenByElevation': lakesTopTenByElevation,
												'lakesTopTenByArea': lakesTopTenByArea})
	