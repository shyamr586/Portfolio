from django.conf.urls import url
from django.urls.resolvers import URLPattern
from firstapp import views

urlpatterns = [
    url(r"^$",views.index,name="home"),
]