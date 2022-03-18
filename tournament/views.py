from rest_framework import viewsets

from .seriallazers import TournamentSerializer
from .models import Tournament

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('name')
    serializer_class = TournamentSerializer