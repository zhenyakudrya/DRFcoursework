from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Класс для сериализации пользователя"""

    class Meta:
        model = User
        fields = ["id", "name", "email", "telegram_id"]