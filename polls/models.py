import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User,
                               related_name='poll_author',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Choice')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
