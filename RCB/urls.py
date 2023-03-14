from RCB.views import *
from django.urls import path

app_name = 'Bittu'

urlpatterns = [
    path('Virat/', Virat, name='Virat'),
]
