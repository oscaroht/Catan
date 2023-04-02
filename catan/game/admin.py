from django.contrib import admin
from .models import *

admin.site.register([Game, Graph, Player, Board, Nodes])

