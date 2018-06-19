# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^poll_state$', views.poll_state,name='poll_state'),
    url(r'^', views.home, name='home'),
]
