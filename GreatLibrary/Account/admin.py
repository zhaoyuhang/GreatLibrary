from django.contrib import admin
from .models import UserInfo, Message, Note

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Message)
admin.site.register(Note)