from django.shortcuts import render
from usersManager.forms import LoginForm

# Create your views here.
def index(request):
    login_form = LoginForm()
    return render(request,'home/index.html',{'login_form':login_form,'in_users_management':False})
def contact_us(request):
    login_form = LoginForm()
    return render(request,'home/contactus.html',{'login_form':login_form,'in_users_management':False})
def documentation(request):
    login_form = LoginForm()
    return render(request,'home/doc.html',{'login_form':login_form,'in_users_management':False})
