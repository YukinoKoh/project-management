from django.contrib import admin
from .models import Choice, Question, Issue, Task
from django.forms import TextInput, Textarea
from django.db import models


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes':['collapse']}),
    ]
    inlines = [ChoiceInline] 
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class TaskInline(admin.TabularInline):
    model = Task
    fields = ['task_title', 'status', 'priority']
    ordering = ('priority',)


class IssueAdmin(admin.ModelAdmin):
    # shown col in the dashboard table
    list_display = ('issue_title', 'status', 'review', 'priority')
    ordering = ('priority',)
    list_filter = ['status', 'review']
    # fold the sub info in detail pate
    fieldsets = [
        ('Status information', {'fields':['status', 'review', 'priority',
                                          'submitted_date'],
                                'classes':['collapse']}),
        (None, {'fields':['issue_title', 'objective', 'description']}),
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'status', 'priority')
    ordering = ('priority',)
    list_filter = ['status']
    # fold the sub info in detail pate
    fieldsets = [
        ('Status information', {'fields':['status', 'priority',
                                          'submitted_date'],
                                'classes':['collapse']}),
        (None, {'fields':['issue', 'task_title', 'description']}),
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Task, TaskAdmin)
