from django.contrib import admin
from django.urls import path,include
from allusers import views
from django.contrib.auth import views as auth_views

from skillvalley.settings import TEMPLATES

urlpatterns = [
    path('login',views.login,name='login'),
    path('joinin',views.joinin,name='joinin'),
    # path('login',views.login,name='login'),
    # path('joinin',views.joinin,name='joinin')
    
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name='reset_password'),
    
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
    name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name="password_reset_confirm"),
    
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),
    name="password_reset_complete"),
]
