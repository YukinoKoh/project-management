import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Issue(models.Model):
    issue_title = models.CharField(max_length=200)
    STATUS_LIST = (('Draft', 'Draft'),
                   ('Ready to review', 'Ready to review'),
                   ('Approved', 'Approved'),
                   ('In Progress', 'In Progress'),
                   ('Done', 'Done'))
    status = models.CharField(max_length=15, choices=STATUS_LIST, default='Draft')  
    priority = models.IntegerField(default=1)
    submitted_date = models.DateTimeField('submitted date', default=timezone.now)
    objective = models.TextField(max_length=400, default='Objective is not defined.')
    description = models.TextField(max_length=800, default='description is not defined.')
    def __str__(self):
        return self.issue_title
    def flow_check(self):
        check_status = self.status
        for t in self.task_set.all():
            return t.status


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    STATUS_LIST = (('Open', 'Open'),
                   ('In Progress', 'In Progress'),
                   ('Done', 'Done'))
    status = models.CharField(max_length=8, choices=STATUS_LIST, default='Open')
    priority = models.IntegerField(default=1)
    submitted_date = models.DateTimeField('date submitted', default=timezone.now)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    description = models.TextField(max_length=800, default='description is not defined.')
    def __str__(self):
        return self.task_title
