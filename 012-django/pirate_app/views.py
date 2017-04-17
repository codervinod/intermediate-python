from django.shortcuts import render
from django.http import HttpResponse, Http404


def translate(request, text):
    text = text.replace('+', ' ')
    if text.lower() != 'hello world':
        raise Http404('I can only translate "hello world".')
    pirate_talk = text.lower().replace('hello', 'ahoy')

    # return HttpResponse(pirate_talk)
    return render(request, 'translate.html', dict(pirate_talk=pirate_talk))
