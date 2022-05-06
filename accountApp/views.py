from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 기존 장고 방식

def hello_world(request):
    return HttpResponse('Hello_world!') # 간단한 응답 객체

# DRF 방식
