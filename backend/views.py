from rest_framework import viewsets, generics
from backend.models import Number, Pokemon
from backend.serializers.NumberSerializers import NumberSerializer
from backend.serializers.PokemonSerializer import PokemonSerializer


import random
import string

class NumberViewSet(viewsets.ModelViewSet):

    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    def get_queryset(self):
        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        return queryset

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def get_queryset(self):

        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        return queryset

class CreateRandomNumber(generics.CreateAPIView):
    serializer_class = NumberSerializer

    def perform_create(self, serializers):
        random_number = random.randint(1, 100)
        random_letter = random.choice(string.ascii_uppercase)
        serializers.save(number=random_number, letter=random_letter)