from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact-us',views.contact_us,name='contact-us'),
    url(r'^doc',views.documentation,name='documentation')
]
