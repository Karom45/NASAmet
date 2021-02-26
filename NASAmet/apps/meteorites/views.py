from django.shortcuts import render
from .models import Meteorite
from django.http import Http404,HttpResponseRedirect


def index(request):
    meteorites_list = Meteorite.objects.order_by('name')[:20]
    return render(request, 'meteorites/list.html', {'meteorites_list': meteorites_list})


def detail(request, meteor_id):
    try:
        meteor = Meteorite.objects.get(meteorite_id=meteor_id)
    except:
        raise Http404("Метеорит не обнаружен")

    return render(request, 'meteorites/detail.html', {'meteor': meteor})