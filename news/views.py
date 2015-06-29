from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def index(request):
    contex = RequestContext(request)
    t = get_template('base.html')
    return HttpResponse(t.render(contex))