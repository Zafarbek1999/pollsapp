from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


def index(request, *args, **kwargs):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    pass


def detail(request, *args, **kwargs):
    question = get_object_or_404(Question, pk=kwargs.get('pk'))
    return render(request, 'polls/detail.html', {'question': question})


def results(request, *args, **kwargs):
    question = get_object_or_404(Question, pk=kwargs.get('pk'))
    return render(request, 'polls/results.html', {'question': question})

def vote(request, *args, **kwargs):

    question = get_object_or_404(Question, pk=kwargs.get('pk'))
    try:
        choice = question.choice_set.get(pk=request.POST.get('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

