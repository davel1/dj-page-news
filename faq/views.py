from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import question,answer


def index(request):
    #return HttpResponse("Hello! You see faq")
    
    contex = {}
    contex['q'] = question.objects.all()
    contex['a'] = answer.objects.all()
    return render(request, 'faq.html', contex)

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