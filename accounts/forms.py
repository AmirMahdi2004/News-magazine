from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کاربری',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور',
        })


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کاربری',
        })
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        })
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'avatar',
        )

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'avatar': 'تصویر پروفایل',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل',
            }),

            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }