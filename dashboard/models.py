import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Issue(models.Model):
    issue_title = models.CharField(max_length=200)
    STATUS_LIST = (('Open', 'Open'),
                   ('Progress', 'In Progress'),
                   ('Done', 'Done'))
    status = models.CharField(max_length=8, choices=STATUS_LIST)
    priority = models.IntegerField(default=1)
    submitted_date = models.DateTimeField('date submitted', default=timezone.now)
    objective = models.TextField(max_length=400, default='Objective is not defined.')
    description = models.TextField(max_length=800, default='description is not defined.')
    def __str__(self):
        return self.issue_title


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    STATUS_LIST = (('Open', 'Open'),
                   ('Progress', 'In Progress'),
                   ('Done', 'Done'))
    status = models.CharField(max_length=8, choices=STATUS_LIST)
    priority = models.IntegerField(default=1)
    submitted_date = models.DateTimeField('date submitted', default=timezone.now)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField(max_length=800, default='description is not defined.')
    def __str__(self):
        return self.task_title
