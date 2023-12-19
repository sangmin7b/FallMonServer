from rest_framework import serializers
from .models import User, FallType, FallHistory


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()


class FallTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class FallHistorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    fall_type = FallTypeSerializer()

