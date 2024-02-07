from django.contrib import admin
from .models import Client, Dispatch, Message

admin.site.register(Client)
admin.site.register(Dispatch)
admin.site.register(Message)

