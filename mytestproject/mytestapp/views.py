from datetime import datetime
from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from mytestapp import serializers
from mytestapp.models import interviews, questions, answers
from rest_framework import status
from mytestapp.serializers import (
    QuestionSerializerCreate,
    QuestionSerializerList,
    AnswerSerializerCreate,
    AnswerSerializerList,
    InterviewSerializerInUpDel,
    InterviewSerializerList,
    InterviewSerializerCreate,
    SnippetSerializer,
    UsernameAnswerSerializer)

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.schemas.coreapi import AutoSchema
from django.http import HttpResponse
from rest_framework.response import Response
import json
# Create your views here.


def index(request):
    opros = questions.objects.all()
    content = {"question": opros}
    return render(request, "mytestapp/opros.html", content)


class UserInterviewList(APIView):
    queryset = interviews.objects.all()

    def get(self, request, pk):
        #userlist = []
        #questionlist = []
        # interview = interviews.objects.raw(
        #    "select i.iname, i.description, i.id  from public.mytestapp_interviews as i where edate >= CURRENT_DATE")

        # for item in interview:
        #    question = questions.objects.raw(
        #        f"select q.text,q.type, q.id from public.mytestapp_questions as q where q.interview_id = {item.id} ")
        #    for qitem in question:
        #        questionlist.append(
        #            {'text': qitem.text, 'type': qitem.type, 'id': qitem.id})
        #    userlist.append({'iname': item.iname, 'desc': item.description,
        #                    'interview_id': item.id, 'question': questionlist})
        #    questionlist = []
        interview = interviews.objects.get(id=pk)
        Serializer = InterviewSerializerList(interview)
        return Response(Serializer.data)


class UserAnswerCreate(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = AnswerSerializerCreate
    queryset = answers.objects.all()


class UserAnswersList(APIView):
    #queryset = answers.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        queryset = answers.objects.filter(pk=pk)
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)


class UsernameAnswersList(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, username):
        queryset = answers.objects.filter(username=username)
        serializer = UsernameAnswerSerializer(queryset, many=True)
        return Response(serializer.data)


class MyQuestioncreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = QuestionSerializerCreate
    queryset = questions.objects.all()


class MyAnswercreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = AnswerSerializerCreate
    queryset = answers.objects.all()


class MyInterviewcreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = InterviewSerializerCreate
    queryset = interviews.objects.all()


class MyQuestionListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializerList
    queryset = questions.objects.all()


class MyAnswerListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializerList
    queryset = answers.objects.all()


class MyInterviewListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = InterviewSerializerList
    queryset = interviews.objects.all()


class MyQuestionInUpDelAPIView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAdminUser,)
    serializer_class = QuestionSerializerList
    queryset = questions.objects.all()


class MyAnswerInUpDelAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = AnswerSerializerList
    queryset = answers.objects.all()


class MyInterviewInUpDelAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = InterviewSerializerInUpDel
    queryset = interviews.objects.all()
