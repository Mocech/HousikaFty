from django.urls import path,include
from . import views
from auth_system.views import  activate, resend_activation
from django.contrib.auth.views import LoginView
from .views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
    login_view
) 


urlpatterns = [
   
   path('register/',views.register,name='register'),
   path("activate/<uidb64>/<token>/", activate, name="activate"), 
   path("resend-activation/", resend_activation, name="resend_activation"),
   # path('accounts/', include('allauth.urls')),
   path('login/',login_view, name='login'),
   # path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
   path('logout/', views.User_logout, name='logout'),
   path('google-login/', views.google_login, name='google-login'),
   
   path('password-reset/',
       PasswordResetView.as_view(template_name ='registration/password_reset.html'),
        name='password_reset'),
    path('password-reset-done/',
        PasswordResetDoneView.as_view(template_name ='registration/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name ='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
     path('password-reset-complete/',
        PasswordResetCompleteView.as_view(template_name ='registration/password_reset_complete.html'),
        name='password_reset_complete'),

   
]