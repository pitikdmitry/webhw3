# coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from views import main_func, hot_func, tag_func, question_func, login_func, signup_func, ask_func


urlpatterns = [
    url(r'^$', main_func, name='main'), # список новых вопросов url = /
    url(r'^hot/$', hot_func, name='hot'), # список лучших вопросв url = /hot/
    url(r'^tag/(?P<tag_id>[0-9]+)/$', tag_func, name='tag'), # список вопросов по тегу url = /tag/blablabla
    url(r'^question/(?P<question_id>[0-9]+)/$', question_func, name='question'),  # страница одного впороса со списком овтптов

    url(r'^login/$', login_func, name='login'),  # форма логина url = /login/
    url(r'^signup/$', signup_func, name='signup'),  # форма регитсрации url = /signup/
    url(r'^ask/$', ask_func, name='ask'),  # форма создания вопроса url = /ask/
]

