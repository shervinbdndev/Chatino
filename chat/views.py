from typing import Union

from django.urls.base import reverse
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from .forms import LoginForm, RegisterForm
        
        






class UserLoginView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        login_form: LoginForm = LoginForm()
        
        if (request.user.is_authenticated):
            return redirect(to=reverse('rooms'))
        
        return render(
            request=request,
            template_name='auth/login.html',
            context={
                'login_form': login_form,
            }
        )
    
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        login_form: LoginForm = LoginForm(request.POST or None)
        if (login_form.is_valid()):
            cd = login_form.cleaned_data
            user = authenticate(
                request=request,
                username=cd['username'],
                password=cd['password'],
            )
            if (user is not None):
                login(
                    request=request,
                    user=user,
                )
                return redirect(to=reverse('rooms'))
            else:
                login_form.add_error(
                    field='username',
                    error='نام کاربری با این مشخصات وجود ندارد',
                )
        return render(
            request=request,
            template_name='auth/login.html',
            context={
                'login_form': login_form,
            },
        )
    
    
    






class UserRegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        register_form: RegisterForm = RegisterForm()
        
        if (request.user.is_authenticated):
            return redirect(to=reverse('rooms'))
        
        return render(
            request=request,
            template_name='index.html',
            context={
                'register_form': register_form,
            }
        )
    
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        register_form: RegisterForm = RegisterForm(request.POST or None)
        if (register_form.is_valid()):
            cd = register_form.cleaned_data
            if (cd['password'] != cd['con_password']):
                register_form.add_error(
                    field='password',
                    error='رمز ورود شما با یکدیگر مطابقت ندارد',
                )
            elif (User.objects.filter(username=cd['username']).exists()):
                register_form.add_error(
                    field='username',
                    error='این نام کاربری قبلا استفاده شده است',
                )
            else:
                user = User.objects.create_user(
                    username=cd['username'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],
                    password=cd['password'],
                    is_active=True,
                )
                user.save()
                return redirect(to=reverse(viewname='login'))
        else:
            register_form.add_error(
                field='password',
                error='اطلاعات خواسته شده به درستی وارد نشده',
            )
        return render(
            request=request,
            template_name='index.html',
            context={
                'register_form': register_form,
            },
        )
        
        
        
        
        
        
        
                
class UserLogoutView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        logout(request=request)
        return redirect(to=reverse('login'))