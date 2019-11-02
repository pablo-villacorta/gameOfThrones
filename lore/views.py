from django.shortcuts import render
from django.views.defaults import page_not_found
import requests
import json
from . import apiHandler as api

def index(request):
    houses = api.getAllHouses()
    return render(request, 'lore/cover.html', {
        "houses": houses
    })

def house(request, name):
    house = api.getHouse(name)
    if (house == None):
        return handler404(request, None)
    characters = api.getCharacters(name)
    return render(request, 'lore/house.html', {
        "house": house,
        "characters": characters
    })

def character(request, name):
    character = api.getCharacterByName(name)
    if character == None: return handler404(request, None)
    return render(request, 'lore/character.html', {
        "character": character
    })

def handler404(request, exception):
    return render(request, 'lore/404.html', status=404)