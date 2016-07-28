from django.conf.urls import url
from . import views


app_name = 'usersManager'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^login',views.login_form,name='login_home'),
    url(r'^logout',views.logout,name='logout_user'),
    url(r'^registration',views.register_user,name='register_user'),


]
