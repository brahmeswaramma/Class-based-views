"""
URL configuration for class_based_views project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun_view/',fun_view,name='fun_view'),
    path('cls_view/',cls_view.as_view(),name='cls_view'),

    path('fbv_view/',fbv_view,name='fbv_view'),
    path('cbv_view/',cbv_view.as_view(),name='cbv_view'),

    path('insertion_fbv/',insertion_fbv,name='insertion_fbv'),
    path('insert_school_by_cbv/',insert_school_by_cbv.as_view(),name='insert_school_by_cbv'),


    path('cbv_view/',cbv_view.as_view(),name='cbv_view')
]