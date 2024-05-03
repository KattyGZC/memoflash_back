from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserModelSerializer
from memo_cards.models import Topic


class RegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        serializer.validated_data['password'] = make_password(password)
        serializer.validated_data.pop('password_confirm')
        serializer.save()

class LoginAPIView(TokenObtainPairView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        user = serializer.user
        token = serializer.validated_data

        response_data = {
            'token': token,
            'user_id': user.id,
            'user_name': user.full_name
        }
        return Response(response_data)
