from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login



class UserAdminCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "id": "email",
            "placeholder": "Enter your email"
        }),
        label="Email"
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "id": "phone_number",
            "placeholder": "Enter your phone number"
        }),
        label="Phone Number"
    ) 
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password1",
            "placeholder": "Enter your password"
        }),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password2",
            "placeholder": "Confirm your password"
        }),
        label="Confirm Password"
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'phone_number', 'password1', 'password2']

class UserLoginForm(forms.Form):  # Remove AuthenticationForm inheritance
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email",
        "id": "email",
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control", 
            "id": "password", 
            "placeholder": "Password"
        }),
        label="Password"
    )  


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request from kwargs
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(self.request, username=email, password=password)  # ✅ Now request is available
            if not user:
                raise forms.ValidationError("Invalid email or password")

        return cleaned_data  
        
        
