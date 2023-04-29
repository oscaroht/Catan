from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
import django

class Game(models.Model):
    name = models.TextField(default='No Name')
    creation_date = models.DateTimeField(default=django.utils.timezone.now())

    def __str__(self):
        return self.name

class Player(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    invite_accept_status = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Board(models.Model):
    # Useful to set up the board colors
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tile_id = models.IntegerField()
    commodity = models.TextField()
    number = models.IntegerField()

class Graph(models.Model):
    node1_id = models.IntegerField()
    node2_id = models.IntegerField()
    edge_id = models.IntegerField()

class Nodes(models.Model):
    # Useful for the payout
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    node_id = models.IntegerField()
    player_id = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    tile1_id = models.IntegerField()
    tile2_id = models.IntegerField()
    tile3_id = models.IntegerField()
