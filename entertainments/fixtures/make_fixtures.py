import json

from data import ENTERTAINED as ent_data


def write(data, filename):
    with open(f'{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load(file_path):
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data


def make_categories():
    fixture = []

    for i, category in enumerate(sorted(ent_data.keys()), start=1):
        obj = {
            'model': 'entertainments.category',
            'pk': i,
            'fields': {
                'name': category,
            },
        }
        fixture.append(obj)

    write(fixture, 'categories')


def make_genres():
    fixture = []
    data_genres = []

    for items in ent_data.values():
        for item in items:
            data_genres.extend(item['genres'])

    more_genres = [
        'sci-fi',
        'thriller',
        'mystery',
        'horror',
        'romance',
        'biography',
        'sports',
        'politics',
        'history',
        'indie',
        'pop',
        'rock',
        'punk',
        'experimental',
        'instrumental',
        'drama',
        'fiction',
    ]
    genres = set(data_genres + more_genres)

    for i, genre in enumerate(sorted(genres), start=1):
        obj = {
            'model': 'entertainments.genre',
            'pk': i,
            'fields': {
                'name': genre,
            },
        }
        fixture.append(obj)

    write(fixture, 'genres')


def make_items():
    fixture = []
    data = ent_data.copy()

    genres = {g['fields']['name']: g['pk'] for g in load('genres.json')}
    categories = {g['fields']['name']: g['pk'] for g in load('categories.json')}

    for category, items in data.items():
        for item in items:
            item['category'] = categories[category]

    all_items = [item for _, items in data.items() for item in items]
    all_items.sort(key=lambda x: x['title'])

    for i, item in enumerate(all_items, start=1):
        obj = {
            'model': 'entertainments.item',
            'pk': i,
            'fields': {
                'title': item['title'],
                'creators': item['creators'],
                'year': item['year'],
                'category': item['category'],
                'genres': [genres[g] for g in item['genres']],
            },
        }
        fixture.append(obj)

    write(fixture, 'items')


if __name__ == '__main__':
    make_items()
