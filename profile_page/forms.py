from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Fornavn')
    last_name = forms.CharField(max_length=100, help_text='Etternavn')
    email = forms.EmailField(max_length=150, help_text='Epost')
    is_pro = forms.BooleanField(required=False, help_text="Profesjonell")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'is_pro', 'password1', 'password2',)
