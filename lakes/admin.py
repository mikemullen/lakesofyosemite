from django.contrib import admin

from .models import Lake
from .models import Drainage
from .models import Trailhead

@admin.register(Lake)
class LakeAdmin(admin.ModelAdmin):
	list_display = ['name', 'elevation']

@admin.register(Drainage)
class DrainageAdmin(admin.ModelAdmin):
	list_display = ['name', 'flows_into']

@admin.register(Trailhead)
class TrailheadAdmin(admin.ModelAdmin):
	list_display = ['name']
