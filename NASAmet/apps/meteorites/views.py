from django.shortcuts import render, get_object_or_404
from .models import Meteorite, Classes
from django.http import Http404, HttpResponseRedirect


def index(request):
    return render(request, 'meteorites/index.html')


def meteorites_list(request):
    meteor_list = Meteorite.objects.order_by('name')[:20]
    return render(request, 'meteorites/list_meteorites.html', {'meteorites_list': meteor_list})


def detail_met(request, meteor_id):
    meteor = get_object_or_404(Meteorite, pk=meteor_id)
    return render(request, 'meteorites/detail_met.html', {'meteor': meteor})


def classes_list(request):
    class_list = Classes.objects.order_by('class_name')[:20]
    #class_dict = {a.class_name: a.classes_id for a in class_list}
    return render(request, 'meteorites/list_classes.html', {'list': class_list})


def detail_class(request, classes_id):
    _class = get_object_or_404(Classes, pk=classes_id)
    linked_meteorites = _class.meteorite_set.all()[:20]
    return render(request, 'meteorites/detail_class.html', {'class': _class, 'list': linked_meteorites})