from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    def __str__(self):
        return self.question_text

class Exam(models.Model):
    title = models.CharField(max_length=50, blank=True)
    edited = models.DateTimeField('Edited', auto_now=True, blank=True, null= True)
    created = models.DateTimeField('Created',auto_now_add=True, blank= True, null= True)

    question = models.ManyToManyField(Question)
    def __str__(self):
        return str(self.id)

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    edited = models.DateTimeField('Edited', auto_now=True, blank=True, null= True)
    created = models.DateTimeField('Created',auto_now_add=True, blank= True, null= True)
    def __str__(self):
        return str(self.id)
        
class SelectedChoice(models.Model):
    exam = models.ManyToManyField(Exam)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    selectedChoice_text = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.selectedChoice_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text





