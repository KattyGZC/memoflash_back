from rest_framework import serializers

from .models import Topic, Card, Item

class CardModelSerializer(serializers.Serializer):
    class Meta:
        model = Card
        fields = (
            'id',
        )