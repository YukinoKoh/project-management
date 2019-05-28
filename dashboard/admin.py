from django.contrib import admin
from .models import Choice, Question, Issue
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


class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Issue, IssueAdmin)
