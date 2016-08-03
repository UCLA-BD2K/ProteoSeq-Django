from django.conf.urls import url
from . import views


app_name = 'analysis'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^main',views.index,name='main'),
    url(r'^sign_auth_aws',views.sign_auth_aws,name = 'aws_sign')



]
