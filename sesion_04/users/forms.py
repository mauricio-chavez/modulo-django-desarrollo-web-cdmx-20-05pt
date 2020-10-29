"""Users app forms"""

from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Signup form"""
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField()
    password_confirmation = forms.CharField()

    def clean_username(self):
        """Checks if username doesn't exist"""
        username = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            raise forms.ValidationError(
                'El usuario ya existe en nuestros registros.'
            )

        return username

    def clean_email(self):
        """Checks if email doesn't exist"""
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError(
                'El correo ya existe en nuestros registros.'
            )

        return email

    def clean(self):
        """Checks that passwords matches"""
        data = self.cleaned_data
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return data

    def save(self):
        """Saves user into database"""
        data = self.cleaned_data
        del data['password_confirmation']
        return User.objects.create_user(**data)
