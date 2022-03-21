from rest_framework import serializers

from .models import Tournament

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('name', 'start_date', 'completeness')