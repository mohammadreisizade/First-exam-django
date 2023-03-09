from django.contrib import admin
from .models import Choice, Question, Exam, SelectedChoice, Score
# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Exam)
admin.site.register(SelectedChoice)
admin.site.register(Score)

