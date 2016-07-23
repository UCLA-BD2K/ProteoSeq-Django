from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


app_name = 'usersManager'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^',views.login_form,name='login_home'),


]
