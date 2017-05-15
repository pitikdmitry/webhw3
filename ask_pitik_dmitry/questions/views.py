from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import fulling_sql_method
from models import Profile, Questions, Tags, Answers, Like



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
    popular_tags = Tags.objects.get_popular_tags()
    questions = Questions.objects.get_new_questions()
    page = paginate(questions, request)
    questions = page
    return render(request, 'main.html', {'page': page, 'questions': questions, 'popular_tags': popular_tags})

def hot_func(request):
    popular_tags = Tags.objects.get_popular_tags()
    questions = Questions.objects.get_new_questions()
    page = paginate(questions, request)
    questions = page
    return render(request, 'hot.html', {'page': page, 'questions': questions, 'popular_tags': popular_tags})


def hot_func(request):
    return render(request, 'hot.html' )


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

