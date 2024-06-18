from rest_framework import viewsets, generics
from backend.models import Number
from backend.serializers.NumberSerializers import NumberSerializers  # Asegúrate de que el archivo se llama 'number_serializer.py'

import random
import string

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializers
    
    def get_queryset(self):
        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        return queryset
    
class CreateRandomNumber(generics.CreateAPIView):
    serializer_class = NumberSerializers
    
    def perform_create(self, serializer):
        random_number = random.randint(1, 100)  # Corrige 'randit' a 'randint'
        random_letter = random.choice(string.ascii_uppercase)
        serializer.save(number=random_number, letter=random_letter)

    