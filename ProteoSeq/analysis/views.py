from django.shortcuts import render
from usersManager.forms import LoginForm
from django.http import HttpResponse
from .credentials import public_key,secret_key
import base64
import hashlib
import hmac

# Create your views here.
def index(request):
    login_form = LoginForm()
    return render(request,'analysis/index.html',{'login_form':login_form,'in_users_management':False,'public_key':public_key})

def sign_auth_aws(request):
    to_sign = str(request.GET['to_sign']).encode('utf-8')
    signature = base64.b64encode(hmac.new(bytes(secret_key), to_sign, hashlib.sha1).digest())
    res = HttpResponse()
    res['Content-Type'] = "text/HTML"
    res.write(signature)
    return res
