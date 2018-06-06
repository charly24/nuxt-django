from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User._meta.pk.name,
            User.USERNAME_FIELD,
            'scope',
        )
        read_only_fields = (User.USERNAME_FIELD,)

    scope = serializers.SerializerMethodField()

    def get_scope(self, user):
        if user.is_superuser:
            return ['admin']
        else:
            return ['general']
