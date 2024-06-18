from rest_framework import serializers
from backend.models import Number

class NumberSerializers(serializers.ModelSerializers):
    number = serializers.Integerfield(required=False)
    letter = serializers.Charfield(max_lenght=100, required=False)
    class Meta:
        model = Number
        fields = ['number', 'letter']