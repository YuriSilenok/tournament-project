from rest_framework import viewsets

from .serialazer import TournamentSerializer
from .models import Tournament

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('name')
    serializer_class = TournamentSerializer