from rest_framework import serializers
from .models import Formateur, Formation, Stagiaire, Inscription
from rest_framework import serializers
from .models import NoteFormation

class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = '__all__'

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'
    def get_moyenne_note(self, obj):
        moyenne = NoteFormation.objects.filter(formation=obj).aggregate(Avg('note'))['note__avg']
        return round(moyenne, 2) if moyenne else 0

class StagiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stagiaire
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'

class NoteFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteFormation
        fields = '__all__'
