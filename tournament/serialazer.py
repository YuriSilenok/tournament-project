from rest_framework import serializers

from .models import Tournament

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id', 'name', 'start_date', 'completeness')