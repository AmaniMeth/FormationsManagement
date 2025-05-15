from rest_framework import viewsets
from .models import Formateur, Formation, Stagiaire, Inscription
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from django.utils import timezone


class FormateurViewSet(viewsets.ModelViewSet):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer

class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

    @action(detail=False, methods=['get'], url_path='search')
    def search_by_title(self, request):
        keyword = request.query_params.get('q', '')
        results = Formation.objects.filter(titre__icontains=keyword)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)

class StagiaireViewSet(viewsets.ModelViewSet):
    queryset = Stagiaire.objects.all()
    serializer_class = StagiaireSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

@api_view(['GET'])
def stats_counts(request):
    count_formateurs = Formateur.objects.count()
    count_stagiaires = Stagiaire.objects.count()
    count_formations = Formation.objects.count()
    return Response({
        'nombre_formateurs': count_formateurs,
        'nombre_stagiaires': count_stagiaires,
        'nombre_formations' : count_formations
    })
@api_view(['GET'])
def inscriptions_per_formation(request):
    data = Formation.objects.annotate(
        nb_inscriptions=Count('inscription')
    ).values('id', 'titre', 'nb_inscriptions')
    return Response(list(data))

@api_view(['GET'])
def stagiaires_par_formation(request, formation_id):
    inscriptions = Inscription.objects.filter(formation_id=formation_id).select_related('stagiaire')
    stagiaires = [{'id': i.stagiaire.id, 'nom': i.stagiaire.nom, 'email': i.stagiaire.email} for i in inscriptions]
    return Response(stagiaires)


@api_view(['GET'])
def formations_a_venir(request):
    today = timezone.now().date()
    formations = Formation.objects.filter(date_debut__gt=today).values('id', 'titre', 'date_debut', 'date_fin')
    return Response(list(formations))

