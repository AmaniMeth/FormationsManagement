from rest_framework import serializers
from .models import Formateur, Formation, Stagiaire, Inscription
from rest_framework import serializers
from .models import NoteFormation
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterStagiaireSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Stagiaire
        fields = ['user', 'nom', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        stagiaire = Stagiaire.objects.create(user=user, **validated_data)
        return stagiaire

class RegisterFormateurSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Formateur
        fields = ['user', 'nom', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        formateur = Formateur.objects.create(user=user, **validated_data)
        return formateur
