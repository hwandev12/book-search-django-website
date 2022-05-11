from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import Profile, UserModel
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
    # fields we want to include and customize in our form
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
        }))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
        }))
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control',
                             }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1',
            'password2'
        ]
# create user online form
class UserFrom(forms.ModelForm):
    class Meta:
        model = UserModel    
        fields = (
            "name",
            "last_name",
            "email",
            "age",
            "agent",
        )
