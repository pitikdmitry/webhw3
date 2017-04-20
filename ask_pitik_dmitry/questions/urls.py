# coding=utf-8
import django.conf.urls
from django.conf import settings

import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.main_func, name='main'), # список новых вопросов url = /
    django.conf.urls.url(r'^hot/(?P<hot_id>[0-9]+)/$', views.hot_func, name='hot'), # список лучших вопросв url = /hot/
    django.conf.urls.url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag_func, name='tag'), # список вопросов по тегу url = /tag/blablabla
    django.conf.urls.url(r'^questions/(?P<question_id>[0-9]+)/$', views.question_func, name='question'),  # страница одного впороса со списком овтптов

    django.conf.urls.url(r'^login/$', views.login_func, name='login'),  # форма логина url = /login/
    django.conf.urls.url(r'^signup/$', views.signup_func, name='signup'),  # форма регитсрации url = /signup/
    django.conf.urls.url(r'^ask/$', views.ask_func, name='ask'),  # форма создания вопроса url = /ask/
    django.conf.urls.url(r'^settings/$', views.settings_func, name='settings'),
]
