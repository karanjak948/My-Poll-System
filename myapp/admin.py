from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Define how the fields appear in the form
    fieldsets = [
        (None, {"fields": ["question_text"]}),  # Ensure 'question_text' field is correct
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # Inline related models (Choice model in this case)
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
