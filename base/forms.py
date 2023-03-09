from django.forms import ModelForm
from .models import Choice, Exam, Question

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class CreateQuestionForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'