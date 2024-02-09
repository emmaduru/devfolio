import re
import validators
from django.core.exceptions import ValidationError


def validate_github(value):
    """Raise a ValidationError if the link is 
    not a github link.
    """
    if "github.com" not in value:
        msg = 'Must be a github profile.'
        raise ValidationError(msg)

def validate_kaggle(value):
    """Raise a ValidationError if the link is 
    not a kaggle link.
    """
    if "kaggle.com" not in value:
        msg = 'Must be a kaggle profile.'
        raise ValidationError(msg)

def validate_website(value):
    """Raise a ValidationError if the link is 
    not a valid link.
    """
    if not validators.url(value):
        msg = "Must be a valid website link"
        raise ValidationError(msg)