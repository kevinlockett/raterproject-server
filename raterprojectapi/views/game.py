from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game

class GameView(ViewSet):
    """Rater Project games view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = SingleGameSerializer(game)
            return Response(serializer.data)

        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """
        games = Game.objects.all()   
        serializer = MultiGameSerializer(games, many=True)
        return Response(serializer.data)

class SingleGameSerializer(serializers.ModelSerializer):
    """JSON serializer for retrieving, adding, or editing a single game"""
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'est_time_to_play', 'age_recommendation', 'player']
        
class MultiGameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Game
        # fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type_id', 'gamer_id')
        fields = '__all__'
        depth = 1