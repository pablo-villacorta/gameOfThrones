from app.models import Character, House, Episode
from rest_framework import viewsets, generics, filters
from app.serializers import CharacterSerializer, HouseSerializer, EpisodeSerializer

# Search by ID
class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

# Search by Name
class CharacterNameView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class HouseNameView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class EpisodeNameView(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

# Search by ID
class CharacterIDView(generics.ListCreateAPIView):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class HouseIDView(generics.ListCreateAPIView):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = House.objects.all()
    serializer_class = HouseSerializer