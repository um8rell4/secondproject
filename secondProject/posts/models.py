from django.db import models


class Posts(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:50]

# Create your models here.
