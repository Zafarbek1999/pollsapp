from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request, *args, **kwargs):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, *args, **kwargs):
    question = get_object_or_404(Question, pk=kwargs.get('pk'))
    return render(request, 'polls/detail.html', {'question': question})


def results(request, *args, **kwargs):
    return HttpResponse('Hello')


def vote(request, *args, **kwargs):
    return HttpResponse('Hello')
