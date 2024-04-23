from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer,
)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "email", "password", "first_name", "last_name"]


class UserProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ["id", "username", "email", "first_name", "last_name"]
