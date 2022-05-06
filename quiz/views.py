from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello World!")

# 개수가 주어졌을 때, 개수 만큼의 랜덤 퀴즈들을 반환
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id) # totalQuis 리스트에서 개수를 id만큼 설정
    serializer = QuizSerializer(randomQuizs, many=True) # many 옵션 - 다량의 데이터에 대한 직렬화 가능하게 함
    return Response(serializer.data)