from django.conf.urls import re_path
from . import views



app_name='review'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
