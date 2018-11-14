from django.conf.urls import url
from django.contrib import admin

from lakes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^lakes/info/(?P<slug>[-\w]+)/$', views.lake_detail, name='lake_detail'),
    url(r'^lakes/images/(?P<slug>[-\w]+)/$', views.lake_images, name='lake_images'),
    url(r'^lakes_lists/', views.lakes_lists, name='lakes_lists'),
]

