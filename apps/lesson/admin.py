from django.contrib import admin

from .models import question, choice, lesson

class LessonAdmin (admin.ModelAdmin):
  list_display = ["content"]

class QuestionAdmin (admin.ModelAdmin):
  list_display = ["lesson", "question_text"]

class ChoiceAdmin (admin.ModelAdmin):
  list_display = ["questions", "choice_text"]

admin.site.register(lesson.Lesson, LessonAdmin)
admin.site.register(question.Question, QuestionAdmin)
admin.site.register(choice.Choice, ChoiceAdmin)


