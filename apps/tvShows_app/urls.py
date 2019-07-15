from django.conf.urls import url
from . import views, models

urlpatterns = [
    url(r'^shows$', views.index),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
]
