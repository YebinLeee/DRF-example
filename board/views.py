from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

# REST api endpoint
def viewjson(request):
    return JsonResponse('REST API and point...', safe=False)

# 게시글 작성


# 게시판 조회


# 게시물 상세 보기


# 게시물 수정


# 게시물 삭제