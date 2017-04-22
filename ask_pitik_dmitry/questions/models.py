# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.http import Http404
from django.db import models

# Create your models here.

class QuestionManager(models.Manager):
    def get_question_by_id(self, q_id):
        try:
            q = self.get(pk=q_id)
            q.tag_list = self.get_tags_for_question_by_id(q.id)
            q.answers_count = self.get_count_of_answers(q.id)
        except Question.DoesNotExist:
            q = None
            raise Http404("Question does not exist")
        return q

    def get_new_questions(self):
        q_list = self.prefetch_related('user').order_by('-pub_date')[:100]
        return Question.objects.fill_questions(q_list)

    def get_best_questions(self):
        q_list = self.order_by('-rating')[:100]
        return Question.objects.fill_questions(q_list)


class Question(models.Model):
    user = models.ForeignKey('Profile')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag')
    objects = QuestionManager()

class Answer(models.Model):
    user = models.ForeignKey('Profile')
    question = models.ForeignKey('Question')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    #objects = AnswerManager()

class Tag(models.Model):
    name = models.CharField(max_length=255)
    #objects = TagManager()

class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=255)
    #avatar = models.ImageField(upload_to='uploads', null=True, blank=True)
    #objects = ProfileManager()

class Like(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="content_type_likes")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey('Profile')
    like = models.BooleanField()
    #objects = LikeManager()