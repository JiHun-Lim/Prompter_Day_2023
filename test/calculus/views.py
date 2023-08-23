from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from calculus.forms import AnswerForm
from calculus.models import Answer

class ProblemListView(ListView):
    model = Answer
    template_name = "calculus/problem_list.html"


class AnswerDetailView(DetailView):
    model = Answer
    template_name = "calculus/answer_detail.html"


class AnswerCreateView(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = "calculus/answer_create.html"
    success_url = reverse_lazy("problem_list")