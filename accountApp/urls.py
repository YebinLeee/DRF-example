from django.urls import path
from accountApp.views import hello_world

urlpatterns = [
    path('hello_world/', hello_world)
]