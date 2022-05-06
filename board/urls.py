from django.urls import path,include
from .views import viewjson, index, boardlist, boardview, boardinsert, boardupdate, boardelete

urlpatterns = [
    path('', index, name='index'), # index VIEW를 루트로 지정
    path('viewjson/', viewjson, name='viewjson'),
    path('boardlist/', boardlist, name='boardlist'),
    path('boardview/<str:pk>', boardview, name='boardview'),
    path('boardinsert/', boardinsert, name='boardinsert'),
    path('boardupdate/<str:pk>', boardupdate, name='boardupdate'),
    path('boardelete/<str:pk>', boardelete, name='boardelete'),
]
