from django import forms
from django.core import validators


class RoomMessageForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'id': 'username',
                'width': '100px',
                'type': 'hidden',
                'value': '{{ username }}'
            }
        )
    )
    
    room_id = forms.CharField(
        max_length=64,
        required=True,
        label='شماره اتاق',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'id': 'roomid',
                'width': '100px',
                'type': 'hidden',
                'value': '{{ room_details.id }}'
            }
        )
    )
    
    message = forms.CharField(
        max_length=1000,
        required=True,
        label='پیام',
        validators=[
            validators.MinLengthValidator(limit_value=1),
            validators.MaxLengthValidator(limit_value=1000),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'id': 'chat-message-input',
                'width': '100px',
            }
        )
    )