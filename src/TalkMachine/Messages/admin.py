from django.contrib import admin
from .models import Message, Vote


admin.site.register(Message)
admin.site.register(Vote)
