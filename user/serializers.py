from rest_framework import serializers

from user.models import Catalog

# -------------------------- Auth ------------------------------------------

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()

class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

# -------------------------- Catalog ------------------------------------------

class CatalogSerializer(serializers.ModelSerializer):
    is_default = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ("id", "type", "name", "photo", "teg", "is_default")   # user не редагується напряму
        read_only_fields = ('id',)

    def get_is_default(self, obj)->bool:
        return obj.user is None

class DefaultValueCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultValueCatalog
        fields = ["comment", "weight", "price", "d", "h", "w"]

# -------------------------- Cosmonauts ------------------------------------------
