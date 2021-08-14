from django.contrib import admin

from .models import Category, Genre, Item

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Item)
