from rest_framework import permissions
from .models import Stagiaire, Formateur

class IsFormateur(permissions.BasePermission):
    def has_permission(self, request, view):
        return Formateur.objects.filter(user=request.user).exists()

class IsStagiaire(permissions.BasePermission):
    def has_permission(self, request, view):
        return Stagiaire.objects.filter(user=request.user).exists()
