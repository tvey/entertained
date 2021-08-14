from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ['title', 'category', 'creators', 'year', 'genres']
