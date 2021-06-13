from django.db.models.fields import SlugField
from rest_framework import fields, serializers
from mytestapp.models import *


class QuestionSerializerCreate(serializers.ModelSerializer):
    interview = serializers.SlugRelatedField(
        slug_field='iname', read_only=True)

    class Meta:
        model = questions
        fields = '__all__'


class AnswerSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = answers
        fields = '__all__'


class InterviewSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = interviews
        fields = '__all__'


class QuestionSerializerList(serializers.ModelSerializer):

    class Meta:
        model = questions
        fields = ('text', 'type', 'interview')


class AnswerSerializerList(serializers.ModelSerializer):

    # user = serializers.SlugField()
    question = serializers.SlugRelatedField(slug_field="text", read_only=True)

    class Meta:
        model = answers
        fields = ('type', 'username', 'dates', 'text_q', 'question')


class InterviewSerializerList(serializers.ModelSerializer):
    question = QuestionSerializerCreate(many=True)

    class Meta:
        model = interviews
        fields = ('iname', 'bdate', 'edate', 'description', 'question')


class InterviewSerializerInUpDel(serializers.ModelSerializer):

    class Meta:
        model = interviews
        fields = ('iname', 'edate', 'description')
        read_only_fields = ['bdate']


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = answers
        fields = ('username', 'type', 'question', 'dates', 'text_q')


class UsernameAnswerSerializer(serializers.ModelSerializer):

    question = QuestionSerializerCreate()

    class Meta:
        model = answers
        fields = ('username', 'text_q', 'dates', 'question')
