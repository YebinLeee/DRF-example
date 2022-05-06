from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Board
from .serializers import Board
from django.utils import timezone

# REST api endpoint
def viewjson(request):
    return JsonResponse('REST API and point...', safe=False)

# 인덱스
@api_view(['GET'])
def index(request):
    timeBoards = []
    for _ in range(10):
        time = timezone.now()
        timeBoards.append(time)
        
    api_urls = {
        'List' : '/boardlist/',
        'Detail' : '/boardview/<str:pk>',
        'Create' : '/boardinsert',
        'Update' : '/boardupdate/<str:pk>',
        'Delete' : '/boardelete/<str:pk>',
        'boards' : timeBoards,
    }
    return Response(api_urls)

# 게시글 작성


# 게시판 조회


# 게시물 상세 보기


# 게시물 수정


# 게시물 삭제