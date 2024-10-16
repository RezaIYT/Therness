from rest_framework import serializers

class CalculationInputSerializer(serializers.Serializer):
    input_data = serializers.FloatField()

class CalculationResultSerializer(serializers.Serializer):
    result = serializers.FloatField()
