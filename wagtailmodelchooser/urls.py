from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^chooser/(?P<app_label>[a-zA-Z0-9_]+)/(?P<model_name>[a-zA-Z0-9_]+)/$',
        views.chooser,
        name='model_chooser'),
    re_path(r'^chooser/(?P<app_label>[a-zA-Z0-9_]+)/(?P<model_name>[a-zA-Z0-9_]+)/(?P<filter_name>.+)/$',
        views.chooser,
        name='model_chooser'),
]
