from django.shortcuts import render, redirect,get_object_or_404
from django.middleware.csrf import get_token
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.signing import TimestampSigner, BadSignature
from auth_system.form import UserAdminCreationForm
from auth_system.models import CustomUser
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages 
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.core.signing import Signer
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from .form import UserLoginForm 
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)



# from .form import CustomLoginForm
# import logging


CustomUser = get_user_model()  # Get the custom user model



def register(req):
    form = UserAdminCreationForm()
    if req.method == 'POST':
        form = UserAdminCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            # user.phone_number = form.cleaned_data['phone_number']
            user.save()
            
          
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            current_site = get_current_site(req)
            activation_link = f"http://{current_site.domain}/Auth/activate/{uid}/{token}/"


            subject = f"Verify Your Email - {user.email}"
  
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'activation_link': activation_link
            })

            # Send email properly
            email = EmailMultiAlternatives(
                subject=subject,
                body=f"Click the link to verify your email: {activation_link}",
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
            )
            email.attach_alternative(message, "text/html")
            email.send()

            messages.success(req, "Check your email for a verification link.")
            return redirect('register')


    return render(req, 'registration/register.html', {'form': form})
print("Register view is being called!")  # Debug print





def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # Decode user ID
        user = get_object_or_404(CustomUser, pk=uid)  # Fetch user or return 404
        
        # Verify token
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account has been activated successfully! You can now log in.")
            return redirect('login')

        messages.error(request, "Invalid or expired activation link.")
        return redirect('resend_activation')  # Redirect to resend activation page

    except (ValueError, TypeError):
        messages.error(request, "Invalid activation request.")
        return redirect('resend_activation')
    
signer = Signer()

def resend_activation(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = CustomUser.objects.get(email=email)

            if user.is_active:
                messages.info(request, "Your account is already active. You can log in.")
                return redirect('login')

            # Generate new activation link
            token = signer.sign(user.email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            activation_link = f"http://{current_site.domain}/Auth/activate/{uid}/{token}/"




            # Send email
            subject = "Resend Activation - Sweetify"
            message = f"Click the link to verify your email: {activation_link}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            messages.success(request, "A new activation link has been sent to your email.")
            return redirect('login')

        except CustomUser.DoesNotExist:
            messages.error(request, "No account found with that email.")
            return redirect('resend_activation')  # Ensure a refresh so messages appear

    return render(request, "registration/activation_failed.html")
       
            
            
def User_logout(request):
    
        logout(request)  # Logs the user out
        messages.success(request, "You have been logged out successfully.")  # Adds success message
        return redirect(reverse('login'))           
            
            
def login_view(request):
    form = UserLoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Authenticate using email
            user = authenticate(request, username=email, password=password)  

            if user:
                login(request, user)
                return redirect("home")  # Redirect after successful login
            else:
                form.add_error(None, "Invalid email or password")  # Display error message

    return render(request, "registration/login.html", {"form": form})
            
def google_login(request):
    print("Request URL:", request.build_absolute_uri())  # Prints the URL being accessed by the app
    redirect_uri = request.build_absolute_uri('/accounts/google/login/callback/')
    print("Google Redirect URI:", redirect_uri)  # Prints the redirect URL
    return redirect('/accounts/google/login/')

            
class PasswordResetView(PasswordResetView):
    def form_valid(self, form):
        messages.success(self.request, "We've sent you an email with instructions to reset your password.")
        return super().form_valid(form)

class PasswordResetDoneView(PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        messages.info(request, "If your email exists in our system, you will receive a reset link shortly.")
        return super().get(request, *args, **kwargs)

class PasswordResetConfirmView(PasswordResetConfirmView):
    def form_valid(self, form):
        messages.success(self.request, "Your password has been successfully reset. You can now log in with your new password.")
        return super().form_valid(form)
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        
        # Check if the link is invalid after calling dispatch
        if hasattr(self, "validlink") and not self.validlink:
            if not any(message.message == "The password reset link is invalid or has expired. Please request a new one below." for message in messages.get_messages(request)):
                messages.error(
                    self.request,
                    "The password reset link is invalid or has expired. Please request a new one below."
                )
            return redirect("password_reset")  # Redirect instead of returning an invalid context

        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class PasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        messages.success(request, "Password reset complete. You can now log in.")
        return redirect('login')




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            
    