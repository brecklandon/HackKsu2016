from twilio.rest import TwilioRestClient
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

account = "AC91202b7272942acdb0b2afa934264def"
token = "e4be4d15bafe23881e2627b05231dabd"

client = TwilioRestClient(account, token)


@csrf_exempt
def sendMessage(request):
    if request.method == 'POST':
        try:
            body = json.load(request.body)
            print(request.body)
            print(body)

            s = "Your dependent needs help. They are located at " + body.get('2')
            message = client.messages.create(to="+13166702055", from_="+13162029726",
                                     body="message stuff")
            return JsonResponse(status=200, data={'message': 'Message sent.'})
        except:
            print(request.body)
            return JsonResponse(status=400, data={'message': str(request.body)})
    else:
        print('get ' + request.bod)
        return JsonResponse(status=200, data={'message': 'get request received.'})

