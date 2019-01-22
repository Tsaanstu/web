from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from question.models import Question, User, Tag, Like, QuestionManager, Answer
from django.db import models

# Create your views here

def paginator(questions_list, request):
    paginator = Paginator(questions_list, 4)

    page = request.GET.get('page')
    try:
        questions_list = paginator.page(page)
    except PageNotAnInteger:
        questions_list = paginator.page(1)
    except EmptyPage:
        questions_list = paginator.page(paginator.num_pages)
    return questions_list


def tag(request,tag):
    m_tag = Tag.objects.get(title=tag)
    questions_list = Question.objects.filter(tags=m_tag.id)
    questions_list = paginator(questions_list, request)

    return render(request, 'question/tag.html', {"questions": questions_list})

def hot(request):
    questions_list = Question.objects.get_hot()
    questions_list = paginator(questions_list, request)
    return render(request, 'question/hot.html', {"questions": questions_list})


def index(request):
    questions_list = Question.objects.get_new()
    questions_list = paginator(questions_list, request)
    return render(request, 'question/index.html', {"questions": questions_list})

def question(request, id):
    t_question = Question.objects.get(pk=id)
    t_answer = Answer.objects.filter(question=id)
    list = [t_question, t_answer]
    return render(request, "question/question.html", {"question": list})


def ask(request):
    return render(request, "question/ask.html", {})


def registration_page(request):
    return render(request, "question/registration_page.html", {})


def settings(request):
    return render(request, "question/settings.html", {})


def login(request):
    return render(request, "question/login.html", {})