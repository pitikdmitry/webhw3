from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
