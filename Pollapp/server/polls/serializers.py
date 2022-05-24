from pyexpat import model
from rest_framework import serializers
from .models import *


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Choice
        fields = ("question",'choice_text','votes')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Question
        fields = ("questionid","question_text",'pub_date')