from django.conf.urls import url
from . import views


app_name = 'analysis'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^main',views.index,name='main'),



]
