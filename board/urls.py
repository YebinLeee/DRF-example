from django.urls import path,include
from .views import viewjson, index

urlpatterns = [
    path('', index, name='index'), # index VIEW를 루트로 지정
    path('viewjson/', viewjson, name='viewjson')
]
