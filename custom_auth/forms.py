from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.forms import UsernameField
from .models import User


class SignUpForm(forms.ModelForm):
    username = UsernameField(
        max_length=User.USERNAME_MAX_LENGTH,
        min_length=User.USERNAME_MIN_LENGTH,
        strip=True,
        required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, 
        required=True,
        validators=[MinLengthValidator(User.PASSWORD_MIN_LENGTH),
                    MaxLengthValidator(User.PASSWORD_MAX_LENGTH)])
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    
class SignInForm(forms.Form):
    username_or_email = UsernameField(strip=True, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)