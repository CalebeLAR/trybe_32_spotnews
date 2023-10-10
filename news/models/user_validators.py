from django.core.exceptions import ValidationError


def validate_name_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid value: name cannot be empty")


def validate_password_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid value: password cannot be empty")


def validate_email_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid value: email cannot be empty")


def validate_role_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid value: role cannot be empty")
