# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.service_upload import views

urlpatterns = [

    # The home page
    path('', views.image_upload, name='upload'),

]
