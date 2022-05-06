from django.urls import path,include
from .views import viewjson, index, boardlist, boardview

urlpatterns = [
    path('', index, name='index'), # index VIEW를 루트로 지정
    path('viewjson/', viewjson, name='viewjson'),
    path('boardlist/', boardlist, name='boardlist'),
    path('boardview/<str:pk>', boardview, name='boardview'),
]
