from rest_framework import serializers

from user.models import Catalog, DefaultValueCatalog, DefaultResourceCatalog, Resource, Material, Teg, TegProject


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

class DefaultResourceCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultResourceCatalog
        fields = ('id', 'resource', 'value', 'is_disposable')
        read_only_fields = ('id',)

# -------------------------- Cosmonauts ------------------------------------------



class ResourcesSerializer(serializers.ModelSerializer):
    is_default = serializers.SerializerMethodField()
    class Meta:
        model = Resource
        fields = ('id', 'name', 'icon', 'measurement', 'limit', 'is_limit_type_big', 'stock', 'is_stock_percentage', 'is_default')
        read_only_fields = ('id',)

    def get_is_default(self, obj)->bool:
        return obj.user is None


class MaterialsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Material
        fields = ('id','name', 'photo')
        read_only_fields = ('id',)




class TegsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = ('id', 'name')
        read_only_fields = ('id',)


class TegProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TegProject
        fields = ('id', 'name')
        read_only_fields = ('id',)
