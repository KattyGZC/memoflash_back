from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User



class UserRegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)


    def validate(self, data):
        if data.get('password') != data.get('password_confirm'):
            raise serializers.ValidationError("Passwords must match")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserLoginSerializer(TokenObtainPairSerializer):
    username_field = User.get_email_field_name()

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['is_admin'] = user.is_superuser
        return token


class UserModelSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'email,'
            'full_name',
        )
