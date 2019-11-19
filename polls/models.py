import datetime

from django.db import models
from django.utils import timezone


class QuestionManager(models.Manager):
    pass


class Question(models.Model):
    objects = QuestionManager()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return '{} {}'.format(self.question_text, self.pub_date)

    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'


class ChoiceManager(models.Manager):
    pass


class Choice(models.Model):
    objects = ChoiceManager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text




