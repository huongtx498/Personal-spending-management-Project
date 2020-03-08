from django.urls import path
from .views import tienich


urlpatterns = [
    path('', tienich, name='tienich_page'),
]