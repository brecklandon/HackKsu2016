from twilio.rest import TwilioRestClient
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect

account = "AC91202b7272942acdb0b2afa934264def"
token = "e4be4d15bafe23881e2627b05231dabd"

client = TwilioRestClient(account, token)


def sendMessage(request):
    if request.method == 'POST':
        try:
            message = client.messages.create(to="+13166702055", from_="+13162029726",
                                     body="Your dependent needs help. They are located at..")
            return JsonResponse(status=200, message='Message sent.')
        except:
            return JsonResponse(status=400, message='something failed')
    return HttpResponseRedirect(reverse('takecare:index'))

