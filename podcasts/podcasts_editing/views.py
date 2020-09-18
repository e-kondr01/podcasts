from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import PhotoForm, AudioForm


def index(request):
    return HttpResponse('this is a page')


@csrf_exempt
def podcast(request):
    if request.method == 'POST':
        q = request.GET.get('document', default=0)
        if q == 'photo':
            form = PhotoForm(request.POST, request.FILES)
            for filename, file in request.FILES.items():
                name = request.FILES[filename].name

            if form.is_valid():
                form.save()
                res = {}
                res['result'] = 'success'
                res['address'] = f'https://podcasts-editing.herokuapp.com/photo/{name}'
                return JsonResponse(res)
            else:
                res = {}
                res['result'] = 'fail'
                res['reason'] = 'form not vailid'
                return JsonResponse(res)
        elif q == 'audio':
            form = AudioForm(request.POST, request.FILES)
            for filename, file in request.FILES.items():
                name = request.FILES[filename].name

            if form.is_valid():
                form.save()
                res = {}
                res['result'] = 'success'
                res['address'] = f'https://podcasts-editing.herokuapp.com/audio/{name}'
                return JsonResponse(res)
            else:
                res = {}
                res['result'] = 'fail'
                res['reason'] = 'form not vailid'
                return JsonResponse(res)
        elif not q:
            res = {}
            res['result'] = 'fail'
            res['reason'] = 'no query param'
            return JsonResponse(res)
    else:
        res = {}
        res['result'] = 'fail'
        res['reason'] = 'method not POST'
        return JsonResponse(res)


def edit(request):
    return HttpResponse('edit')


def photo(request, name):
    try:
        with open(f'photos/{name}.jpg', "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except FileNotFoundError:
        res = {}
        res['result'] = 'fail'
        res['reason'] = 'file not found'
        return JsonResponse(res)


def audio(request, name):
    try:
        with open(f'audios/{name}', "rb") as f:
            return HttpResponse(f.read(), content_type="audio/mpeg")
    except FileNotFoundError:
        res = {}
        res['result'] = 'fail'
        res['reason'] = 'file not found'
        return JsonResponse(res)
