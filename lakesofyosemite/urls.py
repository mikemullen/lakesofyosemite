from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from lakes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^lakes/info/(?P<slug>[-\w]+)/$', views.lake_detail, name='lake_detail'),
    url(r'^lakes/images/(?P<slug>[-\w]+)/$', views.lake_images, name='lake_images'),
    url(r'^lakes_lists/', views.lakes_lists, name='lakes_lists'),
    url(r'^about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

