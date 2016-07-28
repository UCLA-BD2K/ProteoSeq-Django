from django.shortcuts import render
from usersManager.forms import LoginForm
# Create your views here.
def index(request):
    login_form = LoginForm()
    return render(request,'analysis/index.html',{'login_form':login_form,'in_users_management':False})
