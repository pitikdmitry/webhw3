from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = {
    '1': {'id': 1, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real'},
    '2': {'id': 2, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal'},
    '3': {'id': 3, 'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel'},
}


def main_func(request, main_id):
    return render(request, 'ask.html', {'questions': QUESTIONS.values()})

def hot_func(request, hot_id):
    response = "You're looking at the results of hot %s."
    return render(request, 'hot_page.html', {'question': QUESTIONS.get(hot_id, {})})

def tag_func(request, tag_id):
    return HttpResponse("You're voting on tag %s." % tag_id)

def question_func(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def login_func(request, login_id):
    response = "You're looking at the results of login %s."
    return HttpResponse(response % login_id)

def signup_func(request, signup_id):
    return HttpResponse("You're voting on signup %s." % signup_id)

def ask_func(request, ask_id):
    return HttpResponse("You're voting on ask %s." % ask_id)
