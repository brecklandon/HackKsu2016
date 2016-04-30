from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?i)add/$', views.add, name="add"),
    url(r'^(?i)remove/$', views.remove, name="remove"),
]