from django.contrib import admin
from .models import Issue, Task
from django.forms import TextInput, Textarea
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class TaskInline(admin.TabularInline):
    model = Task
    fields = ['task_title', 'status', 'priority']
    ordering = ('priority',)
    show_change_link = True


class IssueAdmin(admin.ModelAdmin):
    # shown col in the dashboard table
    list_display = ('issue_title', 'status', 'priority')
    ordering = ('priority',)
    list_filter = ['status']
    # fold the sub info in detail pate
    fieldsets = [
        ('Status information', {'fields':['priority',
                                          'submitted_date'],
                                'classes':['collapse']}),
        (None, {'fields':['status', 'issue_title', 'objective', 'description']}),
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    def link_to_Issue(self, obj):
        link=reverse("admin:dashboard_issue_change", args=[obj.issue_id]) 
        #model name has to be lowercase
        return mark_safe(u'<a href="%s">%s</a>' % (link, obj.issue))

    list_display = ('task_title', 'link_to_Issue', 'status', 'priority')
    ordering = ('priority',)
    list_filter = ['status', 'issue']
    # fold the sub info in detail pate
    fieldsets = [
        ('Status information', {'fields':['priority',
                                          'submitted_date'],
                                'classes':['collapse']}),
        (None, {'fields':['status', 'issue', 'task_title', 'description']}),
    ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


# Register your models here.
admin.site.register(Issue, IssueAdmin)
admin.site.register(Task, TaskAdmin)
