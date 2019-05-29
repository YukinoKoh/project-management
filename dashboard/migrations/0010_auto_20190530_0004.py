# Generated by Django 2.1.7 on 2019-05-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20190529_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='review',
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Ready to review', 'Ready to review'), ('Approved', 'Approved'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Draft', max_length=15),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'In Progress'), ('3', 'Done')], max_length=8),
        ),
    ]
