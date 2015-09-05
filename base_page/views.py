from django.shortcuts import render
from django.template import RequestContext
from .models import People, Honors, GroupList, ModDate
from django.template.loader import get_template
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

def context_decan_show(request):
    contex = {}
    try:
        decan_obj = People.objects.get(position = 'Decan')
    except:
        pass
    contex.update({'decan_obj': decan_obj})
    c = ModDate.objects.get(pk=1)
    contex.update({'moddate': c.get_mod()})
    return contex

def index(request):
    contex = RequestContext(request)
    t = get_template('base.html')
    return HttpResponse(t.render(contex))


def groups_list(request):
    g = GroupList.objects.all()
    contex = RequestContext(request)
    contex.update({'gl': g})
    t = get_template('gl.html')
    return HttpResponse(t.render(contex))

def groups_details(request, id):
    try:
        g = GroupList.objects.get(pk = id)
    except:
        raise Http404("No user!")
    c = Honors.objects.filter(student = g)
    contex = RequestContext(request)
    contex.update({'gl': g})
    contex.update({'c': c})
    t = get_template('gl_details.html')
    return HttpResponse(t.render(contex))

def honor_details(request, id, hon):
    try:
        g = GroupList.objects.get(pk = id)
    except:
        raise Http404("No user!")
    try:
        c = Honors.objects.get(pk = hon)
    except:
        raise Http404("No honor!")
    contex = RequestContext(request)
    contex.update({'c': c})
    t = get_template('honor_details.html')
    return HttpResponse(t.render(contex))

def profile(request):
    contex = RequestContext(request)
    t = get_template('profile.html')
    return HttpResponse(t.render(contex))