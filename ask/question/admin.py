from django.contrib import admin

from question.models import Question, User, Tag, Like, Answer

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Answer)