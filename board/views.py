from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Board
from .serializers import BoardSerializer
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


# 게시판 조회
@api_view(['GET'])
def boardlist(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    
    return Response(serializer.data)


# 게시물 상세 보기
@api_view(['GET'])
def boardview(request, pk):
    boards = Board.objects.get(id=pk)
    serializer = BoardSerializer(boards, many=False) # False로 지정
    
    return Response(serializer.data)
'''

# 게시글 작성
@api_view(['POST'])
def create(request):
    


# 게시물 수정
@api_view(['PUT'])
def update(request, id):
    

# 게시물 삭제
@api_view(['DELETE'])
def delete(request, id):
    board = Board.get.object(id=id)
    board.delete()
    
'''