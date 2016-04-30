from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?i)login/$', views.login_view, name="login"),
    url(r'^(?i)logout/$', views.logout_view, name="logout"),
]