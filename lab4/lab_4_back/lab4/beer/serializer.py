from rest_framework import serializers
from .models import Company

class MySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Company
        fields = '__all__'