from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated():
        HttpResponseRedirect(reverse('takecare:index'))
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        else:
            print('invalid login')
        return HttpResponseRedirect(reverse('takecare:index'))
    else:
        return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('takecare:index'))