from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


# register form here
class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", )
        field_classes = {'username': UsernameField}