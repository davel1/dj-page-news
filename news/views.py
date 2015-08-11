from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse
from .models import article
# Create your views here.
def index(request):
    contex = RequestContext(request)
    t = get_template('news.html')
    return HttpResponse(t.render(contex))

def context_news_list(request):
    context = {}
    context['news_article'] = article.objects.all()
    return context