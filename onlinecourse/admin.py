from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Instructor, Learner

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class QuestionInline(admin.TabularInline):
    model = Question
    readonly_fields = ('question_text', 'grade')
    show_change_link = True
    extra = 0

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'grade']
    inlines = [ChoiceInline]
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
