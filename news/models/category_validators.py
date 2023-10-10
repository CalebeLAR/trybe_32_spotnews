from django.core.exceptions import ValidationError


def validate_name_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("invalid name: name cannot be empty")


# def v(vale):
#     if not vale:
#         print("if not vale")

#     if len(vale) == 0:
#         print("len(vale) == 0")

#     if vale is None:
#         print("if vale is None")


# v("")
