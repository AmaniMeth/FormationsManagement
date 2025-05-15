from rest_framework import serializers
from .models import Formateur, Formation, Stagiaire, Inscription

class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = '__all__'

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'

class StagiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stagiaire
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'
