from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password_confirm')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(),
        }
