from rest_framework.serializers import ModelSerializer
from .models import Nutricional

# class NutricionalSerializer(ModelSerializer):
#     class Meta:
#         model = Nutricional
#         fields = '__all__'
        
class NutricionalSerializer(ModelSerializer):
    class Meta:
        model = Nutricional
        fields = ['prato', 'valorEnergetico', 'carboidratos', 'proteinas', 'gordurasTotais', 'gordurasSaturadas', 'gordurasTrans', 'fibraAlimentar', 'sodio']
        # extra_kwargs = {'prato': {'write_only': True}}