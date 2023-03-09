# Generated by Django 4.0.5 on 2022-07-06 07:39

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_questionanswer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.CharField(choices=[(django.db.models.fields.Field.value_from_object, 'option1'), (django.db.models.fields.Field.value_from_object, 'option2'), (django.db.models.fields.Field.value_from_object, 'option3'), (django.db.models.fields.Field.value_from_object, 'option4')], max_length=100, null=True),
        ),
    ]