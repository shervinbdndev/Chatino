from django.urls.base import reverse
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

from .models import Room, Message
from .forms import RoomMessageForm







class RoomsView(View):
    def get(self, request: HttpRequest) -> HttpRequest:
        return render(
            request=request,
            template_name='rooms.html',
            context={
                'rooms': Room.objects.all(),
            },
        )
        
        
        




class RoomDetailView(View):
    def get(self, request: HttpRequest, slug) -> HttpRequest:
        room_message_form: RoomMessageForm = RoomMessageForm()
        room: Room = Room.objects.get(slug=slug)
        messages: Message = Message.objects.filter(room=room)[0:25]
        
        return render(
            request=request,
            template_name='room-detail.html',
            context={
                'room': room,
                'messages': messages,
                'room_message_form': room_message_form,
            }
        )
        
    def post(self, request: HttpRequest, slug):
        room_message_form: RoomMessageForm = RoomMessageForm(request.POST or None)
        room: Room = Room.objects.get(slug=slug)
        messages: Message = Message.objects.filter(room=room)[0:25]
        
        if (not room_message_form.is_valid()):
            return redirect(to=reverse('room_detail'))
            
        return render(
            request=request,
            template_name='room-detail.html',
            context={
                'room': room,
                'messages': messages,
                'room_message_form': room_message_form,
            }
        )