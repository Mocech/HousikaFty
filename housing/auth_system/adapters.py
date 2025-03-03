from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect
import socket

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        try:
            # Continue normal login
            super().pre_social_login(request, sociallogin)
            messages.success(request, "Login successful! Welcome back.")
        except socket.timeout:
            messages.error(request, "Connection timeout. Please check your internet and try again.")
            return redirect("account_login")  # Redirect back to login
        except Exception as e:
            messages.error(request, "An unexpected error occurred. Please try again later.")
            return redirect("account_login")
