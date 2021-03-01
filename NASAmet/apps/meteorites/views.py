from django.shortcuts import render, get_object_or_404
from .models import Meteorite, Classes
from django.urls import reverse
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
    return render(request, 'meteorites/list_classes.html', {'list': class_list})


def detail_class(request, classes_id):
    _class = get_object_or_404(Classes, pk=classes_id)
    linked_meteorites = _class.meteorite_set.all()[:20]
    return render(request, 'meteorites/detail_class.html', {'class': _class, 'list': linked_meteorites})


def add_class(request):
    if request.method == "POST":
        _id = Classes.objects.latest('classes_id').classes_id + 1
        new_class = Classes(classes_id=_id, class_name=request.POST['class_name'], information=request.POST['add_inf'])
        new_class.save()
        return HttpResponseRedirect(reverse('meteorites:classes_list'))
    return render(request, 'meteorites/add_class.html')


def change_class(request ,classes_id):
    _class = get_object_or_404(Classes, pk=classes_id)
    if request.method == "POST":
        _class.class_name = request.POST['class_name']
        _class.information = request.POST['add_inf']
        _class.save()
        return HttpResponseRedirect(reverse('meteorites:detail_class' , args = (_class.classes_id,)))
    return render(request, 'meteorites/change_class.html',{'class': _class})


def delete_class(request ,classes_id):
    _class = get_object_or_404(Classes, pk=classes_id)
    _class.delete()
    return HttpResponseRedirect(reverse('meteorites:classes_list'))


def add_meteorite(request):
    pass
    if request.method == "POST":
        _id = Meteorite.objects.latest('meteorite_id').meteorite_id + 1
        new_meteor = Meteorite(meteorite_id=_id, name=request.POST['class_name'], information=request.POST['add_inf'])
        new_meteor.save()
        return HttpResponseRedirect(reverse('meteorites:classes_list'))
    return render(request, 'meteorites/add_class.html')