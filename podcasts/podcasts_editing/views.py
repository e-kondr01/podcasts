from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .editing_tools import slice_audio, add_fade, combine_audio
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('this is a page')


@csrf_exempt
def podcast(request):
    if request.method == 'POST':
        q = request.GET.get('document', default=0)
        if q == 'photo':
            _id = 1
            f = open(f'{_id}.jpg', 'wb')
            f.write(request.POST.get('photo'))
            f.close()
            res = {}
            res['result'] = 'success'
            res['address'] = f'https://dashboard.heroku.com/apps/podcasts-editing/photo/{_id}'
            return JsonResponse(res)
        elif q == 'audio':
            _id = 2
            f = open(f'{_id}.mp3', 'wb')
            f.write(request.POST.get('audio'))
            f.close()
            res = {}
            res['result'] = 'success'
            res['address'] = f'https://dashboard.heroku.com/apps/podcasts-editing/audio/{_id}'
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


def photo(request, _id):
    try:
        with open(f'{_id}.jpg', "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except FileNotFoundError:
        res = {}
        res['result'] = 'fail'
        res['reason'] = 'file not found'
        return JsonResponse(res)


def audio(request, _id):
    with open(f'{_id}', "rb") as f:
        return HttpResponse(f.read(), content_type="audio/mpeg")
    except FileNotFoundError:
        res = {}
        res['result'] = 'fail'
        res['reason'] = 'file not found'
        return JsonResponse(res)
