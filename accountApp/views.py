from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.


# 기존 장고 방식

def hello_world(request):
    # return HttpResponse('Hello_world!') # 간단한 응답 객체
    return render(request, 'accountapp/temp.html')

# DRF 방식

@api_view() # 데코레이터
def hello_world_drf(request):
    return Response({'message': "Hello, world!"})  # json형태의 dict형태로 응답