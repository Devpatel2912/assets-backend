from rest_framework import serializers
from .models import CategoryMasters
from .models import DeptMasters
from .models import ProductMasters
from .models import LocationMasters
class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMasters
        fields = ['cid', 'name']

class ProductAddSerializer(serializers.Serializer):
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    dimensions = serializers.CharField(required=False, allow_null=True)
    cid = serializers.IntegerField()
    description = serializers.CharField(required=False, allow_null=True)
    did = serializers.IntegerField()

class ProductListSerializer(serializers.Serializer):
    productid = serializers.IntegerField()
    name = serializers.CharField()
    quantity = serializers.IntegerField()
    dimensions = serializers.CharField()
    cid = serializers.IntegerField()
    description = serializers.CharField()
    did = serializers.IntegerField()


class StorageListSerializer(serializers.Serializer):
    storageid = serializers.IntegerField()
    productid = serializers.IntegerField()
    lid = serializers.IntegerField()
    did = serializers.IntegerField()
    quantity = serializers.IntegerField()
    description = serializers.CharField(allow_null=True)
    createat = serializers.DateTimeField()
    updateat = serializers.DateTimeField()

class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptMasters
        fields = ['did', 'name', 'remark']


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMasters
        fields = ['lid', 'name', 'did', 'description']