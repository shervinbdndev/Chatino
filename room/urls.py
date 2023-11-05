from django.urls import path
from . import views



urlpatterns = [
    path(
        route='',
        view=views.RoomsView.as_view(),
        name='rooms',
    ),
    
    path(
        route='<slug:slug>/',
        view=views.RoomDetailView.as_view(),
        name='room_detail',
    )
]