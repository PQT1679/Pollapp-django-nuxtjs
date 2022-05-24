from django.urls import path
from .views import *

urlpatterns = [
    path('Choice/<str:questioncode>/', ChoicebyQuestion,name="ChoicebyQuestion"),
    path('questions/', QuestionView,name="Questions"),
    path('updatevote/', Updatevote,name="voteupdate"),
    path('questions/<str:questionid>/', Result,name="result"),
]