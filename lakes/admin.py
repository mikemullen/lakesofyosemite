from django.contrib import admin

from .models import Lake
from .models import Drainage

@admin.register(Lake)
class LakeAdmin(admin.ModelAdmin):
	list_display = ['name', 'elevation']

@admin.register(Drainage)
class DrainageAdmin(admin.ModelAdmin):
	list_display = ['name', 'flows_into']
