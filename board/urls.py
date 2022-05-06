from django.urls import path,include
from .views import viewjson, index, boardlist

urlpatterns = [
    path('', index, name='index'), # index VIEW를 루트로 지정
    path('viewjson/', viewjson, name='viewjson'),
    path('boardlist/', boardlist, name='boardlist'),
]
