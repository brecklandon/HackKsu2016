from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?i)auth/', include('TakeCare.Auth.urls', namespace='auth')),
    url(r'^(?i)helper/', include('TakeCare.Helper.urls', namespace='helper')),
    url(r'^(?i)user/', include('TakeCare.User.urls', namespace='user')),
]