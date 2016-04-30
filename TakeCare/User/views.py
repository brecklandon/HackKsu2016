from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect

from .forms import UserSignup


def index(request):
    return render(request, 'index.html', {'form': UserSignup()})


def create(request):
    if request.method == "POST":
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            print('user created')
        else:
            print(form.errors)
    return HttpResponseRedirect(reverse('takecare:user:index'))


def update(request):
    return render(request, 'index.html', {})


def remove(request):
    return render(request, 'index.html', {})
