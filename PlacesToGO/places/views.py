from django.shortcuts import render, redirect
from .models import Place
import random
from .forms import PlaceForm


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
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('all_places')
    else:
        form = PlaceForm()

    return render(request, 'places/add_place.html', {'form': form})
