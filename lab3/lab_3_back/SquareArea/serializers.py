from rest_framework import serializers

class DivRequestSerializer(serializers.Serializer):
    input_value = serializers.IntegerField()

class DivResponseSerializer(serializers.Serializer):
    output_value = serializers.IntegerField()