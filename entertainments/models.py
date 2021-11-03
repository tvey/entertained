from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


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

    class Meta:
        ordering = ['title']
