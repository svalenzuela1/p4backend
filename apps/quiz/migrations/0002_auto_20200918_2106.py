# Generated by Django 3.1.1 on 2020-09-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice',
        ),
        migrations.AddField(
            model_name='question',
            name='choice_four',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_one',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_three',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_two',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
