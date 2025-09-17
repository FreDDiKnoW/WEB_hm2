from django.shortcuts import render
from .models import Place
import random


def index1(request):
    places = Place.objects.all()
    places_count = places.count()

    show_random = request.GET.get('random', False)

    if not places.exists():
        return render(request, 'places/index1.html', {
            'place': None,
            'places_count': places_count
        })

    if show_random:
        weighted_places = []
        for place in places:
            weighted_places.extend([place] * place.rating)

        random_place = random.choice(weighted_places)

        return render(request, 'places/index1.html', {
            'place': random_place,
            'places_count': places_count
        })
    else:
        return render(request, 'places/index1.html', {
            'place': None,
            'places_count': places_count
        })


def all_places(request):
    places = Place.objects.all()
    return render(request, 'places/all_places.html', {'title': 'WhereToGO', 'places': places})


def add_place(request):
    return render(request, 'places/add_place.html')
