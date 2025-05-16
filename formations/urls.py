from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import noter_formation
from .views import NoteFormationViewSet
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('formations/a_venir/', formations_a_venir, name='formations-a-venir'),  # <-- avant router
]
router = DefaultRouter()
router.register('formateurs', FormateurViewSet)
router.register('formations', FormationViewSet)
router.register('stagiaires', StagiaireViewSet)
router.register('inscriptions', InscriptionViewSet)
router.register('notes', NoteFormationViewSet)


urlpatterns += [
    path('', include(router.urls)),
    path('stats/counts/', stats_counts, name='stats-counts'),
    path('stats/inscriptions_per_formation/', inscriptions_per_formation, name='inscriptions-per-formation'),
    path('formations/<int:formation_id>/stagiaires/', stagiaires_par_formation, name='stagiaires-par-formation'),
    path('formations/noter/', noter_formation, name='noter-formation'),
    path('formations/moyennes_notes/', moyennes_formations, name='moyennes-notes'),
    path('auth/login/', obtain_auth_token, name='login'),
    path('auth/register/stagiaire/', register_stagiaire, name='register-stagiaire'),
    path('auth/register/formateur/', register_formateur, name='register-formateur'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
     path('api/auth/login/', obtain_auth_token, name='api_token_auth'),
    

]
