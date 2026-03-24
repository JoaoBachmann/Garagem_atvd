from rest_framework import serializers

from core.models import veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = veiculo
        fields = '__all__'
