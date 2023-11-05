from django.urls import path
from . import views


urlpatterns = [
    path(
        route='',
        view=views.UserRegisterView.as_view(),
        name='register',
    ),
    
    path(
        route='login/',
        view=views.UserLoginView.as_view(),
        name='login',
    ),
    
    path(
        route='logout/',
        view=views.UserLogoutView.as_view(),
        name='logout',
    ),
]