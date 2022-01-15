from django.conf.urls import url
from django.urls.resolvers import URLPattern
from firstapp import views

app_name = "portfolio"

urlpatterns = [
    url(r"^$",views.index,name="home"),
    url(r"^bio",views.bio,name="bio"),
    url(r"^feedback",views.feedback,name="feedback"),
]