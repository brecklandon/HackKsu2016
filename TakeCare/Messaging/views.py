from twilio.rest import TwilioRestClient
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect

account = "AC91202b7272942acdb0b2afa934264def"
token = "e4be4d15bafe23881e2627b05231dabd"

client = TwilioRestClient(account, token)


def sendMessage(request):

    message = client.messages.create(to="+12023750680", from_="+13162029726",
                                     body="Your dependent needs help. They are located at..")
    return HttpResponseRedirect(reverse('takecare:index'))
