from django.shortcuts import render
from django.views.defaults import page_not_found
import requests
import json

from lore.models import House, Allegiance, Character, Sibling, Relationship

def index(request):
    houses = House.objects.all()
    return render(request, 'lore/cover.html', {
        "houses": houses
    })

def house(request, name):
    try:
        house = House.objects.get(name=name)
    except House.DoesNotExist:
        return handler404(request, None)
    characters = house.characters_in_house.all()
    return render(request, 'lore/house.html', {
        "house": house,
        "characters": characters,
        "allegiance": house.allegiance.all()
    })

def character(request, name):
    try:
        character = Character.objects.get(name=name)
    except Character.DoesNotExist:
        return handler404(request, None)
    return render(request, 'lore/character.html', {
        "character": character,
        "siblings": character._siblings.all(),
        "related": character.related_to.all()
    })

def handler404(request, exception):
    return render(request, 'lore/404.html', status=404)
