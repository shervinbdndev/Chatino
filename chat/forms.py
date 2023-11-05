from django import forms
from django.core import validators
    
    

    
    

class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'username',
        },),
    )
    
    first_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'fname',
        },),
    )
    
    last_name = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,  
        label='نام خانوادگی',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'lname',
        },),
    )
    
    email = forms.EmailField(
        max_length=150,
        required=True,
        label='ایمیل',
        validators=[
            validators.EmailValidator(),
        ],
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'email',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'pass',
        },),
    )
    
    con_password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='تایید رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'conpass',
        },),
    )
    
    



class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=64,
        required=True,
        label='نام کاربری',
        validators=[
            validators.MinLengthValidator(limit_value=3),
            validators.MaxLengthValidator(limit_value=64),    
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'username',
        },),
    )
    
    password = forms.CharField(
        min_length=6,
        max_length=64,
        required=True,
        label='رمز ورود',
        validators=[
            validators.MinLengthValidator(limit_value=6),
            validators.MaxLengthValidator(limit_value=64),
        ],
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'pass'
        },),
    )