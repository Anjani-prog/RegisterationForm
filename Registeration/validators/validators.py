from django.core.exceptions import ValidationError
# from django.utils.transaction import ugettext_lazy as _
import re
from Registeration.models import Users

def validate_email(value):
    if not  "yourdomain.com" in value:
        raise ValidationError(("Email submitted is invalid."))
    return value

def validate_name(value):
    if not bool(re.match('^[a-zA-Z]+$',value)):
        raise ValidationError('This field must not be numeric/special characters')
    return value

def validate_phone(value):
    x = len(value)
    if not x==10 :
        raise ValidationError('phone number must be 10 digits')
    elif not bool(re.match('^[0-9]+$',value)):
        raise ValidationError('This field must not be alphabets/special characters')
    return value