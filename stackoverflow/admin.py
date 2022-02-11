from django.contrib import admin

from .models import CommentedItem, Question, Answer, Tag

admin.site.register([
    Question,
    Answer,
    CommentedItem,
    Tag
])
