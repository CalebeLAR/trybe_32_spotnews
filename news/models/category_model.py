from django.db import models
from news.models.category_validators import validate_name_field


class Categories(models.Model):
    name = models.CharField(max_length=200, validators=[validate_name_field])

    def __str__(self):
        return f"{self.name}"
