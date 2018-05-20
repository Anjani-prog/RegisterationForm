from django import forms

from Registeration.validators import validate_email
from Registeration.validators import validate_name
from Registeration.validators import validate_phone
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class UserForm(forms.Form):

    username = forms.CharField(label='Username', max_length=254)
    first_name = forms.CharField(label='First Name', max_length=254,validators=[validate_name])
    last_name = forms.CharField(label='Last Name', max_length=254,validators=[validate_name])
    email = forms.CharField(label='Email',max_length=128,validators =[validate_email])
    email = forms.EmailField(label='Email', max_length=128)
    phone = forms.CharField(label='phone',validators =[validate_phone])
    file = forms.FileField(label='Select a file',help_text='max. 42 megabytes')
#     install pillow



