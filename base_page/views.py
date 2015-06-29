from django.shortcuts import render
from django.template import RequestContext
from .models import People

# Create your views here.

def context_decan_show(request):
    decan_obj = People.objects.get(position = 'Decan')
    decan_obj
    return {'decan_obj': decan_obj}