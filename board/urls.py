from django.urls import path,include
from .views import viewjson

urlpatterns = [
    path('viewjson/', viewjson, name='viewjson')
]
