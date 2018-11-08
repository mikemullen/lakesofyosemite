from django.conf.urls import url
from django.contrib import admin

from lakes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^lakes/(\d+)/', views.lake_detail, name='lake_detail'),
]
