from rest_framework.serializers import ModelSerializer

from core.models import veiculo


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = veiculo
        fields = '__all__'
