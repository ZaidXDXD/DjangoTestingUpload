from django import forms
from datetime import date 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput, TextInput, boolean_check
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from datetime import date

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={'placeholder': 'Username', 'autocomplete' : 'off'}))
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput(attrs={'placeholder' : 'Email', 'autocomplete' : 'off'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email Or Username', 'autocomplete':'off'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))


class UserForm(forms.ModelForm):
    class Meta:
        models = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'max' : date.today()}))
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        