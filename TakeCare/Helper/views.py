from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required()
def add(request):
    if request.method == 'POST':
        helper = user=get_user_model().objects.get(email=request.POST['email'])
        u = user=get_user_model().objects.get(email=request.user.email)
        if helper and helper.user.email is not u.user.email:
            u.assistants_set.add(helper, bulk=False)

        else:
            print('user not found')
        return HttpResponseRedirect(reverse('takecare:index'))


def remove(request):
    pass
