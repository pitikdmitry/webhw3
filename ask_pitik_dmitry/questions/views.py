from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from models import Questions, Answers, Tags, Profile, Like


questions_pag = []
for i in range(1, 5):
    questions_pag.append({'title': 'title ' + str(i),
                      'id': i,
                      'text': 'text' + str(i)
                      })


def signup_func(request):
    return render(request, 'register.html')


def main_func(request):
    popular_tags = Tags.objects.get_popular_tags()
    questions = Questions.objects.get_new_questions()
    page = paginate(questions, request)
    questions = page
    return render(request, 'hot.html', {'page': page, 'questions': questions, 'popular_tags': popular_tags})


def hot_func(request):
    popular_tags = Tags.objects.get_popular_tags()
    questions = Questions.objects.get_new_questions()
    page = paginate(questions, request)
    questions = page
    return render(request, 'hot.html', {'page': page, 'questions': questions, 'popular_tags': popular_tags})


def tag_func(request, tag_name):
    tag = Tags.objects.get_tag_by_name(tag_name)
    questions = Questions.objects.get_questions_by_tag(tag)
    page = paginate(questions, request)
    questions = page
    return render(request, 'tag.html', {'page': page, 'questions': questions, 'tag': tag})


def question_func(request, question_id):
    question = Questions.objects.get_by_id(question_id)
    answers = Answers.objects.get_answers_by_question_id(question_id)
    return render(request, 'question.html', {'question': question,
                                             'question_id': question_id,
                                             'answers': answers}
                                             )


def login_func(request):
    return render(request, 'login.html', { 'continue': resolve_url('login')})


def settings(request):
    return render(request, 'settings.html')


@login_required(login_url='/questions/login/')
def ask_func(request):
    return render(request, 'ask.html')


def paginate(list_data, request):
    paginator = Paginator(list_data, 3)
    page_num = request.GET.get('page')
    try:
        page = paginator.page(page_num)
        if page_num is not None:
            page_num = int(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
        page_num = 1
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
        page_num = paginator.num_pages
    page.page_range_current = get_page_range(page_num, paginator)
    return page


def get_page_range(current, paginator):
    count = 5
    wing = 2
    if current - wing > 0:
        if current + wing <= paginator.num_pages:
            page_range = range(current - wing, current + wing + 1)
        else:
            page_range = range(current - (count - (paginator.num_pages + 1 - current)), paginator.num_pages + 1)
    else:
        if current + count - 1 <= paginator.num_pages:
            page_range = range(1, count + 1)
        else:
            page_range = range(1, paginator.num_pages + 1)
    return page_range

