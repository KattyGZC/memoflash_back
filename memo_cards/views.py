from memoflash_back.settings import BASE_DIR

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

import pandas as pd

from .models import Topic


def greeting(request):
    return HttpResponse("API MemoFlash")


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
            df = pd.read_csv(f'{BASE_DIR}/src/word_families.csv')
            data = {}
            for index, row in df.iterrows():
                data[str(index)] = [
                    {'title': 'noun', 'content': str(row['Nouns']).title(), 'comment': ''},
                    {'title': 'adjective', 'content': str(row['Adjectives']).title(), 'comment': ''},
                    {'title': 'verb', 'content': str(row['Verbs']).title(), 'comment': ''},
                    {'title': 'adverb', 'content': str(row['Adverbs']).title(), 'comment': ''}
                ]

        return Response(data, status=status.HTTP_200_OK)
