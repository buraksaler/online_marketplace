from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your Password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), required=True)
  

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    
  username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Your username',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), max_length=30, required=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')
  
  email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Your email',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), required=True)
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Your Password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), required=True)
  
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat Password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }), required=True)
  