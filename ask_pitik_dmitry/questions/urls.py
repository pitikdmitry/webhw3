# coding=utf-8
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^ssql/$', views.handle, name='main'),
    url(r'^$', views.main_func, name='main'), # список новых вопросов url = /
    url(r'^hot/(?P<hot_id>[0-9]+)/$', views.hot_func, name='hot'), # список лучших вопросв url = /hot/
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag_func, name='tag'), # список вопросов по тегу url = /tag/blablabla
    url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_func, name='question'),  # страница одного впороса со списком овтптов

    url(r'^login/$', views.login_func, name='login'),  # форма логина url = /login/
    url(r'^signup/$', views.signup_func, name='signup'),  # форма регитсрации url = /signup/
    url(r'^ask/$', views.ask_func, name='ask'),  # форма создания вопроса url = /ask/
    url(r'^settings/$', views.settings_func, name='settings'),
]

