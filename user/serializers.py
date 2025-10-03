from rest_framework import serializers

# -------------------------- Auth ------------------------------------------

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()

class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()