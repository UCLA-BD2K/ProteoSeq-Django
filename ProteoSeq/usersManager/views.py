from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def redirection(next_url):
    if next_url:
        return HttpResponseRedirect(next_url)
    else:
        return HttpResponseRedirect('/')


def login_form(request):
    signin_form = LoginForm(request.POST or None)
    next = request.GET.get('next', None)
    if request.user.is_authenticated():
        return redirection(next)
    if request.POST and signin_form.is_valid():#calls the clean method of LoginForm
        login(request,signin_form.get_logged_in_user())
        return redirection(next)
    if not next:
        next = ""
    return render(request, 'usersManager/login.html', {'signin_form':signin_form, 'redirect_url':next,'in_users_management':True})

@login_required
def logout(request):
    next = request.GET.get('next', None)
    if request.POST:
        django_logout(request)
    return redirection(next)

def register_user(request):
    register_form = RegistrationForm(request.POST or None)
    next = request.GET.get('next', None)
    if request.POST and register_form.is_valid():
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        user = User.objects.create_user(username=username,email=username,password=password1,first_name=first_name,last_name=last_name)
        user = authenticate(username=username,password=password1)
        if user:
            login(request,user)
            return redirection(next)
    else:
        if not next:
            next = ""
    return render(request, 'usersManager/register.html', {'register_form':register_form, 'redirect_url':next,'in_users_management':True})
