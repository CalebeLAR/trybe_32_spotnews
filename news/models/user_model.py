from django.db import models
from .user_validators import (
    validate_name_field,
    validate_email_field,
    validate_password_field,
    validate_role_field,
)


class Users(models.Model):
    name = models.CharField(max_length=200, validators=[validate_name_field])
    email = models.EmailField(
        max_length=200, validators=[validate_email_field]
    )
    password = models.CharField(
        max_length=200, validators=[validate_password_field]
    )
    role = models.CharField(max_length=200, validators=[validate_role_field])

    def __str__(self):
        return f"{self.name}"

    pass
