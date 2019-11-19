from django.urls import path
from django.conf.urls import re_path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    re_path('questlist/$', views.QuestionView.as_view(), name='question-list'),
    re_path('questlist/(?P<pk>[\d]+)/$', views.QuestionInstanceView.as_view(), name='question-instance'),
]