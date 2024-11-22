from rest_framework import serializers
from .models import Person

class PeopeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Person
        fields= '__all__'
        depth=1 