from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)
    search_url = serializers.SerializerMethodField('get_search_url')

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choice_set', 'search_url')

    def get_search_url(self, obj):
        return "https://www.google.com/search?q={}".format(obj.question_text).replace(" ", "")

