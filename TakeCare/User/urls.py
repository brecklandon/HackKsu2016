from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?i)create/$', views.create, name="create"),
    url(r'^(?i)update/$', views.update, name="update"),
    url(r'^(?i)remove/$', views.remove, name="remove"),
]