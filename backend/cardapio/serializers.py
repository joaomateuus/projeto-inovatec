from rest_framework import serializers
from .models import Prato
from nutricional.serializers import NutricionalSerializer

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = ['id', 'nome', 'valor', 'detalhes', 'foto']
        
class PratoNutriSerializer(serializers.ModelSerializer):
    nutricional  = NutricionalSerializer()
    class Meta:
        model = Prato
        fields = ['id', 'nome', 'valor', 'detalhes', 'foto', 'nutricional']