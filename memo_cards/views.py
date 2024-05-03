from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Topic

def greeting(request):
    return HttpResponse("API MemoFlash")

class IndexAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        
        if request.user.is_authenticated:
            data = {}
            topics = Topic.objects.filter(user=request.user)
            data['topics'] = [{'id': topic.id, 'name': topic.name, 'enable': topic.enable} for topic in topics]
            data['count'] = topics.count()
        else:
            data = {
                "message": "Bienvenido a MemoFlash",
                "api_documentation_url": "https://documentacion-de-nuestra-api.com",
                "version": "1.0",
                
            }
        
        return Response(data, status=status.HTTP_200_OK)
    


