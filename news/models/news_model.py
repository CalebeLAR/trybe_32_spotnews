from django.db import models
from news.models.validators import (
    validate_news_title_field,
)


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_news_title_field]
    )
    content = models.TextField()
    author = models.ForeignKey("Users", on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", blank=True)
    categories = models.ManyToManyField(
        "Categories", related_name="news"
    )

    def __str__(self):
        return self.title
