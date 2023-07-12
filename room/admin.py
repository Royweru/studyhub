from django.contrib import admin

from .models import Room, Topic, Message


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','description','updated','created')

class MessageAdmin(admin.ModelAdmin):
    list_display=('user','room','body','updated','created')

admin.site.register(Room,RoomAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Topic)