from CSK.views import *
from django.urls import path

app_name = 'Shubham'

urlpatterns = [
    path('Dhoni/', Dhoni, name='Dhoni'),
]
