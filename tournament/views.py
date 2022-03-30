from rest_framework import viewsets
from .serialazer import TournamentSerializer
from .models import Tournament


def index(request):
	return render(request, '../templates/main.html')

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all().order_by('name')
    serializer_class = TournamentSerializer
