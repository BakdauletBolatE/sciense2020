from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
        username = forms.CharField(label="Есімі",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
        email = forms.EmailField(label="Email",
                                widget=forms.TextInput(
                                    attrs={'class':'form-control',
                                    }))
        password1 = forms.PasswordInput()
        password2 = forms.PasswordInput()

  