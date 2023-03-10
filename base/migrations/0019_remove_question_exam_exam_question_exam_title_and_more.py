# Generated by Django 4.0.5 on 2022-07-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_choice_selected_choice_exam_question_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.AddField(
            model_name='exam',
            name='question',
            field=models.ManyToManyField(to='base.question'),
        ),
        migrations.AddField(
            model_name='exam',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='choice',
            name='selected_choice',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1, null=True),
        ),
    ]
