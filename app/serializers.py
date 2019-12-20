from app.models import Character, House, Episode, Appearance
from rest_framework import serializers

class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name','id')

class HouseAllegianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'name')

class CharacterSerializer(serializers.ModelSerializer):
    house = HouseAllegianceSerializer(read_only=True, many=False)
    father = RelatedSerializer(read_only=True, many=False)
    mother = RelatedSerializer(read_only=True, many=False)
    related = RelatedSerializer(read_only=True, many=True)
    siblings = RelatedSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'actor', 'house', 'father', 'mother', 'image', 'actor', 'slug', 'related', 'siblings')

class HouseSerializer(serializers.ModelSerializer):
    allegiance = HouseAllegianceSerializer(read_only=True, many=True)
    characters_in_house = RelatedSerializer(read_only=True, many=True)

    class Meta:
        model = House
        fields = ('id', 'name', 'words', 'logoURL', 'allegiance', 'characters_in_house')

class EpisodeAppearanceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="character.id")
    name = serializers.CharField(source="character.name")

    class Meta:
        model = Appearance
        fields = ('id', 'name')

class EpisodeSerializer(serializers.ModelSerializer):
    episode_appearance = EpisodeAppearanceSerializer(read_only=True, many=True)

    class Meta:
        model = Episode
        fields = ('id', 'title', 'numberInSeason', 'duration', 'directedBy', 'season', 'episode_appearance')
    