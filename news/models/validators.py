# import re
from django.core.exceptions import ValidationError


def validate_news_title_field(value):
    if len(value) == 0 or value is None:
        raise ValidationError("Este campo não pode estar vazio.")

    if len(value.strip().split(" ")) == 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
