from django.urls import path, include
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Documentation API TEST VIEW For Job')
urlpatterns = [
    #path('', views.index, name='index'),
    path('', schema_view),
    path('question', views.MyQuestioncreateAPIView.as_view(), name='create-question'),
    path('questionlist', views.MyQuestionListAPIView.as_view(), name='questionlist'),
    path('questionInUpDel/<int:pk>/', views.MyQuestionInUpDelAPIView.as_view()),
    path('answer', views.MyAnswercreateAPIView.as_view(), name='create-answer'),
    path('answerlist', views.MyAnswerListAPIView.as_view(), name='answerlist'),
    path('answerInUpDel/<int:pk>/', views.MyAnswerInUpDelAPIView.as_view()),
    path('interview', views.MyInterviewcreateAPIView.as_view(),
         name='create-interview'),
    path('interviewlist', views.MyInterviewListAPIView.as_view(),
         name='interviewlist'),
    path('interviewInUpDel/<int:pk>/', views.MyInterviewInUpDelAPIView.as_view()),
    path('userlist/<int:pk>/', views.UserInterviewList.as_view(), name='user-list'),
    path('useranswerlist' , views.UserAnswersList.as_view()),
    path('useranswercreate', views.UserAnswerCreate.as_view())


]
