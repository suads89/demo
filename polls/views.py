# from django.shortcuts import render
#
# # Create your views here.
# from django.http import HttpResponse
# from .models import Question
# from django.template import loader
# from django.shortcuts import render
# from django.http import Http404
# from django.shortcuts import get_object_or_404
#
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
#
# from .models import Choice, Question
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
from distutils.command.config import config

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.order_by('-pub_date')[:100]
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:100]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        ch = request.POST['choice']
        selected_choice = question.choice_set.get(pk=ch)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def add(request):
    return render(request, 'polls/addNewQuestion.html');


def save(request):
    print("saveeeeeeee")
    if request.method == 'POST':
        print("mmmmmm"+request.POST['qName'])
        try:
            q = Question(question_text= request.POST['qName'])
            q.save()
        except (KeyError):
            return render(request, 'polls/addNewQuestion.html', {
                'error_message': "Error.",
            })
        else:
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:index',))
    else:
        return render(request, 'polls/addNewQuestion.html', {
            'error_message': "No Data Found!!",
        })


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:100]
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponseRedirect(request, 'polls/index.html')