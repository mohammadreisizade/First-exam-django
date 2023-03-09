# Generated by Django 4.0.5 on 2022-08-14 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0026_remove_exam_user_exam_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='score',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]