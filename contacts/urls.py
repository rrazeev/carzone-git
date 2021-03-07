from django.urls import path
from . import  views
from django.contrib import admin
admin.autodiscover()
urlpatterns = [

    path('inquiry', views.inquiry, name='inquiry'),


]