# Generated by Django 4.0.5 on 2022-07-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_questionanswer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.CharField(choices=[('<django.db.models.fields.CharField>', 'option1'), (models.CharField(max_length=100), 'option2'), (models.CharField(max_length=100), 'option3'), (models.CharField(max_length=100, null=True), 'option4')], max_length=100, null=True),
        ),
    ]