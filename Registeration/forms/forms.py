from PIL import Image
from django import forms
from django.forms.widgets import RadioSelect, PasswordInput
from Registeration.validators import *
from django.utils.translation import ugettext_lazy as _


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=254)
    first_name = forms.CharField(label='First Name', max_length=254, validators=[validate_name])
    last_name = forms.CharField(label='Last Name', max_length=254, validators=[validate_name])
    email = forms.CharField(label='Email', max_length=128, validators=[validate_email])
    email = forms.EmailField(label='Email', max_length=128)
    phone = forms.CharField(label='phone', validators=[validate_phone])
    gender = forms.ChoiceField(widget=RadioSelect(), choices=[('male', 'Male'), ('female', 'Female')])
    file = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=20, validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20, help_text=_("Enter the same password as "
                                                                                       "above"", for verification."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password_mismatch")
        return password2
