from specific.views import *
from django.urls import path


app_name='specific'
urlpatterns=[
     path('susil/',susil,name='susil'),
     path('kalia/',kalia,name='kalia')
]

