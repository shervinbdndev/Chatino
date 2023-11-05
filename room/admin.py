from django.contrib import admin

from .models import Room, Message



class RoomModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    

class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'sent_at']

    

admin.site.register(Room, RoomModelAdmin)
admin.site.register(Message, MessageModelAdmin)