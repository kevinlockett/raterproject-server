from rest_framework import status
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from raterprojectapi.models import Category, Game
from datetime import timedelta

class GameTests(APITestCase):
    def setUp(self):
        """
        Create a new Player, collect the auth Token, and create a sample Category
        """
        
        url = '/register'
        
        player = {
            "username": "chappie",
            "password": "myPassword",
            "email": "kevin@lockett.com",
            "address": "777 Infinity Loop",
            "phone_number": "555-6789",
            "first_name": "Kevin",
            "last_name": "Lockett",
            "bio": "Just call me 'Playa!'"
        }
        
        # Initiate POST request and capture the response
        response = self.client.post(url, player, format='json')
        
        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])
        
        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # SEED THE DATABASE WITH A CATEGORY
        # This is necessary because the API does not
        # expose a /categories URL path for creating Categories

        # Create a new instance of Category
        self.category = Category()
        self. category.label = "Board game"
        
        # Save the GameType to the testing database
        self.category.save()
        
        # Create a new instance of GameType at Global Level -- the values can be imported with self. where needed in tests.        
        self.game = Game()
        self.game.title = "Sorry"
        self.game.description = "The Sorry game is known as the game of 'sweet revenge' since players can send each other's pawns back to the starting point"
        self.game.designer = "Hasbro Gaming"
        self.game.year_released = "2021-01-01"
        self.game.number_of_players = 4       
        self.game.est_time_to_play = timedelta(hours=1, minutes=30)
        self.game.age_recommendation = 6
        self.game.player_id = 1

        # Save the Game to the testing database
        self.game.save()
        
    def test_create_game(self):
        """
        Ensure we can create (POST) a new Game.
        """

        # Define the URL path for creating a new Game
        url = "/games"

        # Define the Game properties
        game = {
            "title": "Goat Lords",
            "description": "Hilarious, addictive and competitive card game with goats, of course!",
            "designer": "Gatwick Games",
            "year_released": "2020-12-02",
            "number_of_players": 6,
            "est_time_to_play": "00:01:00",
            "age_recommendation": 7
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, game, format='json')
        
        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(response.data["title"], game['title'])
        self.assertEqual(response.data["description"], game['description'])
        self.assertEqual(response.data["year_released"], game['year_released'])
        self.assertEqual(response.data["number_of_players"], game['number_of_players'])
        self.assertEqual(response.data["est_time_to_play"], game['est_time_to_play'])
        self.assertEqual(response.data["age_recommendation"], game['age_recommendation'])
        
    def test_get_game(self):
        """
        Ensure we can GET an existing game.
        """

        # Define the URL path for getting a single Game
        url = f'/games/{self.game.id}'

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(response.data["title"], self.game.title)
        self.assertEqual(response.data["description"], self.game.description)
        self.assertEqual(response.data["year_released"], self.game.year_released)
        self.assertEqual(response.data["number_of_players"], self.game.number_of_players)
        self.assertEqual(response.data["est_time_to_play"], "01:30:00")
        self.assertEqual(response.data["age_recommendation"], self.game.age_recommendation)
        
    def test_change_game(self):
        """
        Ensure we can change an existing game.
        """

        # Create a new instance of Game
        
        # Save the Game to the testing database
        
        # Define the URL path for updating an existing Game
        url = f'/games/{self.game.id}'

        # Define NEW Game properties
        new_game = {
            "title": "Sorry",
            "description": "More fun than a barrel of monkeys!",
            "designer": "Hasbro Games",
            "year_released": "2021-01-01",
            "number_of_players": 4,
            "est_time_to_play": "00:01:00",
            "age_recommendation": 6
        }
        
        # Initiate PUT request and capture the response
        response = self.client.put(url, new_game, format="json")

        # Assert that the response status code is 204 (NO CONTENT)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(response.data["title"], new_game['title'])
        self.assertEqual(response.data["description"], new_game['description'])
        self.assertEqual(response.data["designer"], new_game['designer'])
        self.assertEqual(
            response.data["year_released"], new_game['year_released'])
        self.assertEqual(
            response.data["number_of_players"], new_game['number_of_players'])
        self.assertEqual(response.data["est_time_to_play"], new_game['est_time_to_play'])
        self.assertEqual(response.data["age_recommendation"], new_game['age_recommendation'])
        
    def test_delete_game(self):
        """Test delete game"""

        url = f'/games/{self.game.id}'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)