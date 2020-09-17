from django.shortcuts import render
from django.http import HttpResponse
from .editing_tools import slice_audio, add_fade, combine_audio

# Create your views here.


def index(request):
    return HttpResponse('this is a page')


def podcast(request):
    q = request.GET.get('document', default=0)
    if q == 'audio':
        return HttpResponse('post audio')
    elif q == 'photo':
        return HttpResponse('post photo')
    elif not q:
        return HttpResponse('all data')


def edit(request):
    return HttpResponse('edit')
