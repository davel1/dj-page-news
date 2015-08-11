from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,Template
# Create your views here.
from .models import question,answer
from django.template.loader import get_template


def index(request):
    contex = RequestContext(request)
    t = get_template('faq.html')
    return HttpResponse(t.render(contex))

def REST_faq_list(Request):
    context = ""
    for x in question.objects.all():
        context += "q:"+x.q
        context += "</br>"
        for y in answer.objects.all():
            if y.child == x:
                context += "a:"+y.r
                context += "</br>"
    return HttpResponse(context)

def context_faq_list(request):
    context = {}
    context['faq_q'] = question.objects.all()
    context['faq_a'] = answer.objects.all()
    return context