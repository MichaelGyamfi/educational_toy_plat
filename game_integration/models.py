from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    # Add fields related to the game
    # Example:
    # description = models.TextField()

class Achievement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Add fields for achievement details
    # Example:
    # description = models.TextField()
    # points = models.PositiveIntegerField()
