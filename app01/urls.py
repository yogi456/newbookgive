from django.conf.urls import url
from . import views

urlpatterns = [
    url("",views.homePage,name="home"),
]
