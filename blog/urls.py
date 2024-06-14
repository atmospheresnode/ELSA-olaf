# Stdlib imports

# Core Django imports
from django.urls import re_path

# Third-party app imports

# Imports from apps
from . import views

app_name='blog'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^archive/', views.archive, name='archive'),
    re_path(r'^post/(?P<pk_post>\d+)/$', views.detail, name='detail'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    re_path(r'^add_category/$', views.add_category, name='add_category'),
    re_path(r'^add_post/$', views.add_post, name='add_post'),
    re_path(r'tasks/$', views.tasks, name='tasks'),
    re_path(r'the_study/$', views.the_study, name='the_study'),

    # ----------------
    #     The following url url messed with the setup of the ELSA archive directory, found in ELSA 
    #     project directory and online at https://atmos.nmsu.edu/elsa/archive/; hence, the issue.  
    #
    #     However, I left this url commented out because I learned about how to nest an argument in
    #     a url.
    #
    # url(r'^archive/(?:detail-(?P<pk>\d+)/)?$', views.detail, name='detail'),
        # (?: ... )? is an outer argument with a nested argument.
        # For more information on what is happening here please see 
        # Nested Arguments @ https://docs.djangoproject.com/en/1.11/topics/http/urls/
    #
    #
    # ----------------
]
