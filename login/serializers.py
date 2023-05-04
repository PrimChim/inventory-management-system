from rest_framework import serializers
from inventory.models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity',
                  'location', 'reorderpoint', 'created_at', 'expirationdate', 'brand']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'email']
