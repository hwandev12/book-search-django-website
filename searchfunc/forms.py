from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

# register form here
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}