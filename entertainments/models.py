from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255)
    creators = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
