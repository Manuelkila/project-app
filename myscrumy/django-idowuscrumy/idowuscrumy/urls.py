from django.contrib import admin
from django.urls import path
from idowuscrumy import views

#path('', views.index) 
#from django.conf.urls import patterns, url

urlpatterns= [
    path('', views.index)
    ]

