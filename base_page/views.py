from django.shortcuts import render
from django.template import RequestContext
from .models import People, Honors, GroupList, ModDate, MyUser
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from news.models import article
from base_page.forms import AddNewForm,AddQForm
from django.utils import timezone
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

@login_required
def profile(request):
    contex = RequestContext(request)
    pf = {}
    if request.user.is_student():
        pf['status'] =  'student'
				# TODO: get status!
    contex.push({'pf':pf})
    form = AddNewForm(request.POST or None)
    contex.update({ 'news_f': form })
    form2 = AddQForm(request.POST or None)
    contex.update({ 'Q_f': form2 })
    t = get_template('profile.html')
    return HttpResponse(t.render(contex))

def signin(request):
    if request.method != 'POST':
        contex = RequestContext(request)
        t = get_template('signin.html')
        return HttpResponse(t.render(contex))
    
    username = request.POST['login']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            raise Http404("disabled account")
    else:
        raise Http404("invalid login")
    
def logout_views(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')

@login_required
def set_stud(request):
    n = request.POST['number']
    try:
        g = GroupList.objects.get(num=int(n))
    except:
        raise Http404("No student")
    try:
        u = MyUser.objects.get(id=request.user.id)
    except:
        raise Http404("No user") 
    u.set_stud(g.name, g.num)
    u.save()
    return HttpResponseRedirect(reverse('profile'))

def add_news(request):
    if request.method == 'POST':
        form = AddNewForm(request.POST)
        #head = form.cleaned_data.get('head', None)
        #text = form.cleaned_data.get('text', None)
        form.save()        
        return HttpResponseRedirect(reverse('news'))
    return HttpResponseRedirect(reverse('profile'))   

def add_q(request):
    if request.method == 'POST':
        form = AddQForm(request.POST)
        form.save()        
        return HttpResponseRedirect(reverse('faq'))
    return HttpResponseRedirect(reverse('profile'))    
