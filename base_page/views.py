from django.shortcuts import render
from django.template import RequestContext
from .models import People
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.

def context_decan_show(request):
    decan_obj = People.objects.get(position = 'Decan')
    decan_obj
    return {'decan_obj': decan_obj}

def index(request):
    contex = RequestContext(request)
    t = get_template('base.html')
    return HttpResponse(t.render(contex))

