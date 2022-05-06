from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Board
from .serializers import BoardSerializer
from django.utils import timezone

# REST api endpoint
def viewjson(request):
    return JsonResponse('REST API and point...', safe=False)

# 인덱스 - api명세 출력
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


# 게시글 작성
@api_view(['POST'])
def boardinsert(request):
    serializer = BoardSerializer(data=request.data)
    
    if serializer.is_valid():
        print('Valid...')
        serializer.save()
    else:
        print('Invalid...') 
        
    return Response(serializer.data)
    

# 게시물 수정
@api_view(['PUT'])
def boardupdate(request, pk):
    boards = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance=board, data=request.data) # False로 지정
    
    if serializer.is_valid():
        print('Valid update...')
        serializer.save()
    else:
        print('Invalid update...') 
        
    return Response(serializer.data)

'''
# 게시물 삭제
@api_view(['DELETE'])
def boarddelete(request, id):
    board = Board.get.object(id=id)
    board.delete()
    
'''