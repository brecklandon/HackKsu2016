from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required()
def add(request):
    if request.method == 'POST':
        if get_user_model().objects.filter(email=request.POST['email']):
            print('found user')
        return HttpResponseRedirect(reverse('takecare:index'))


def remove(request):
    pass
