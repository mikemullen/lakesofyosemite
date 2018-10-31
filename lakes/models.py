from django.db import models

class Lake(models.Model):
	TRAIL_ACCESS_CHOICES = [('Y', 'Yes'), ('N', 'No'), ('S', 'Sort of'), ('R', 'Road Access')]
	name = models.CharField(max_length=100)
	elevation = models.IntegerField(null=True)
	size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	lat = models.DecimalField(max_digits=6, decimal_places=4, null=True)
	lon = models.DecimalField(max_digits=7, decimal_places=4, null=True)
	trailaccess = models.CharField(choices=TRAIL_ACCESS_CHOICES, max_length=1, blank=True)
	drainages = models.ManyToManyField('Drainage', blank=True)

class Drainage(models.Model):
	name = models.CharField(max_length=100)
	flows_into = models.CharField(max_length=100, blank=True)
	terminal = models.BooleanField()


	def __str__(self):
		return self.name