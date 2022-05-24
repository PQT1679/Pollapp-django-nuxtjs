from random import choices
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db.models import F
# Create your views here.
@api_view(['GET'])
def ChoicebyQuestion(request,questioncode):
    queryset= Choice.objects.filter(question=questioncode)
    serializers=ChoiceSerializer(queryset,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def Updatevote(request):
    choice = request.data.get('choice')
    question=choice['question']
    choice_text=choice['choice_text']
    Choice.objects.filter(question=question,choice_text=choice_text).update(votes=F('votes')+1)
    return Response()

@api_view(['GET'])
def QuestionView(request):
    queryset= Question.objects.all()
    serializers=QuestionSerializer(queryset,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def Result(request,questionid):
    queryset= Question.objects.filter(questionid=questionid)
    try:
        questiondata=QuestionSerializer(queryset,many=True).data[0]
        query=Choice.objects.filter(question=questionid)
        choices=ChoiceSerializer(query,many=True).data
        questiondata['choices']=choices
    except:
        pass
    return Response(questiondata)
