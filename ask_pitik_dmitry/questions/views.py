from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import fulling_sql_method
import models.py

def handle(request):
    fillDB = fulling_sql_method.FillDB()
    fillDB.create_func()
    return render(request, 'main.html')

def index(request):
    questions = Question.objects.get_new_questions()
    page = paginate(questions, request)
    questions = page
    popular_tags, popular_users = get_popular()

    return render(request, 'index.html', {
        'questions': questions,
        'page': page,
        'block_title': 'Question Day',
        'popular_tags': popular_tags,
        'popular_users': popular_users,
    })


def main_func(request):
    return render(request, 'main.html')

def hot_func(request, hot_id):
    return render(request, 'hot.html', {'hot_id': hot_id })

def tag_func(request, tag_id):
    return render(request, 'tag.html', {'tag_id': tag_id })

def question_func(request, question_id):
    return render(request, 'question.html', {'question_id': question_id })

def login_func(request):
    return render(request, 'login.html')

def signup_func(request):
    return render(request, 'register.html')

def settings_func(request):
    return render(request, 'settings.html')

def ask_func(request):
    return render(request, 'ask.html')

