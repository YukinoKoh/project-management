# Generated by Django 2.1.7 on 2019-05-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Progress', 'In Progress'), ('Done', 'Done')], max_length=8)),
            ],
        ),
    ]
