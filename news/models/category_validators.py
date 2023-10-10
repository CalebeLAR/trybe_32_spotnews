from django.core.exceptions import ValidationError


def validate_name_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid value: name cannot be empty")
