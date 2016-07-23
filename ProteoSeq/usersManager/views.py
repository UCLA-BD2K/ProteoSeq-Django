from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
# Create your views here.
def login_form(request):
    signin_form = LoginForm(request.POST or None)
    next = request.GET.get('next', None)
    print next
    if request.POST and signin_form.is_valid():#calls the clean method of LoginForm
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect('/')
    else:
        if not next:
            next = ""
        return render(request, 'usersManager/login.html', {'signin_form':signin_form, 'redirect_url':next,'in_login_page':True})
