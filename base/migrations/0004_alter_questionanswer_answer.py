# Generated by Django 4.0.5 on 2022-07-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_questionanswer_trueoption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.CharField(choices=[(models.CharField(max_length=100), 'option1'), ('option2', models.CharField(max_length=100)), ('option3', models.CharField(max_length=100)), ('option4', models.CharField(max_length=100, null=True))], max_length=100, null=True),
        ),
    ]
