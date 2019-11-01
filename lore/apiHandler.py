import requests 

def getAllHouses():
    resp = requests.get("http://api.got.show/api/show/houses")
    resp = resp.json()
    houses = []
    for house in resp:
        if house["name"].startswith("House") and "logoURL" in house:
            houses.append(house)
    return houses

def getHouse(name):
    resp = requests.get("http://api.got.show/api/show/houses/"+name.replace(" ", "%20"))
    resp = resp.json()
    return resp[0]

def getCharacters(house):
    resp = requests.get("https://api.got.show/api/show/characters/byHouse/"+house.replace(" ", "%20"))
    resp = resp.json()
    return resp

def getCharacterByName(name):
    resp = requests.get("https://api.got.show/api/show/characters/"+name.replace(" ", "%20"))
    resp = resp.json()
    return resp