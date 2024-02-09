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

def validate_linkedin(value):
    """Raise a ValidationError if the link is 
    not a linkedin link.
    """
    if "linkedin.com" not in value:
        msg = 'Must be a linkedin profile.'
        raise ValidationError(msg)

def validate_medium(value):
    """Raise a ValidationError if the link is 
    not a medium link.
    """
    if "medium.com" not in value:
        msg = 'Must be a medium profile.'
        raise ValidationError(msg)

