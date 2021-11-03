from django.shortcuts import render
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Genre, Item
from .serializers import ItemSerializer


def index(request):
    """Homepage view with prefilled data."""
    categories = Category.objects.all()
    genres = Genre.objects.all()
    items = Item.objects.all()
    context = {'categories': categories, 'genres': genres, 'items': items}
    return render(request, 'index.html', context)


@api_view(['GET'])
def everything(request):
    """Return serialized data for all items."""
    serializer = ItemSerializer(Item.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filter_data(request):
    """Handle filters and search: get items from db and return serialized."""
    items = {}
    category = request.query_params.get('category')
    genre = request.query_params.get('genre')
    genre_name = request.query_params.get('genreName')
    year_order = request.query_params.get('year')
    search_query = request.query_params.get('q')

    if category:
        items = Item.objects.filter(category=category)
    if genre:
        items = Item.objects.filter(genres__in=[genre]).distinct()
    if genre_name:
        genre_obj = Genre.objects.filter(name=genre_name).first()
        print(genre_obj)
        items = Item.objects.filter(genres__in=[genre_obj]).distinct()
    if year_order == 'old':
        items = Item.objects.order_by('year')
    elif year_order == 'new':
        items = Item.objects.order_by('-year')

    if search_query:
        items = Item.objects.filter(
            Q(title__icontains=search_query)
            | Q(creators__icontains=search_query)
        )
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
