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
    url(r'^lakes/(?P<slug>[-\w]+)/$', views.lake_display, name='lake_display'),
    url(r'^lakes_lists/', views.lakes_lists, name='lakes_lists'),
    url(r'^about/', views.about, name='about'),
    url(r'^notes/', views.notes, name='notes'),
    url(r'^mattie/', views.mattie, name='mattie'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^giving_back/', views.giving_back, name='giving_back'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

