from django.shortcuts import render
from .models import Place


def index1(request):
    return render(request, 'places/index1.html')


def all_places(request):
    Places = Place.objects.all()
    return render(request, 'places/all_places.html', {'title': 'WhereToGO' , 'places': Places})


def add_place(request):
    return render(request, 'places/add_place.html')


def where_to_go(request):
    return render(request, 'places/index4.html')
