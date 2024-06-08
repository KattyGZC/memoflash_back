from memoflash_back.settings import BASE_DIR

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

import pandas as pd

from .models import Topic, Card, Item


def greeting(request):
    return HttpResponse("API Rollacard")


class IndexAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):

        data = {}
        if request.user.is_authenticated:
            user = request.user            
        else:
            user = 1

        topics = Topic.objects.filter(user=user).values(
            'id', 'name', 'enable', 'is_private')
        data['topics'] = [{'id': topic['id'], 'name': topic['name'],
                           'enable': topic['enable'], 'is_private': topic['is_private']} for topic in topics]
        data['count'] = topics.count()

        return Response(data, status=status.HTTP_200_OK)


class ListCardView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk):
        data = {}

        if request.user.is_authenticated:
            user = request.user
        else:
            user = 1
        
        if pk == 1:
            data_cards = Card.objects.filter(topic=1, topic__user=user)
            for card in data_cards:
                data[card.id] = [
                    {
                        'title': item.title, 
                        'content': item.content.title() if item.content.title() else "", 
                        'comment': item.comment.title()
                    } for item in card.items.all()
                ]

        return Response(data, status=status.HTTP_200_OK)
