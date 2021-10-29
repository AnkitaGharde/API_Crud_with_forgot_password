from django.forms import forms
from .models import candidate


class signup(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    class meta:
        models=candidate
        fields =['Firstname', 'Lastname', 'email', 'mobile', 'password']


