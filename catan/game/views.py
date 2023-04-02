from django.shortcuts import render
from django.http import HttpResponse
# from json import dumps
import json
from django.views import View
import random
from .models import Game, Player, Board
from .forms.createnewgame import NewGameForm


def home(request):
    # if request.method == "GET":
    #     data = {1: 'a', 2: 'b', 3: 'c'}
    #     data_json = json.dumps(data)
    #     return render(request, 'game/home.html', {'data': data_json})
    # elif request.method == "POST":
    #     print(request)
    #     print("arrived in the post request handling section")
    #     # request_getdata = request.POST.get("data", None)
    #     # body = request.body.decode('utf-8')
    #     data = json.load(request)
    #     print(data)
    #     print(data['data'])
    return render(request, 'game/home.html')


def create_board(game_id):
    commodity = ["lumber", "lumber", "lumber", "lumber", "wool", "wool", "wool", "wool", "brick", "brick", "brick",
                 "ore", "ore", "ore", "grain", "grain", "grain", "grain"]
    numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]  # len 18
    random.shuffle(numbers)
    random.shuffle(commodity)
    for i in range(1, 19):
        Board(game_id, i, commodity[i], numbers[i])


class CreateNewGameView(View):
    def get(self, request):
        return render(request, 'game/createnewgame.html', {'form': NewGameForm})

    def post(self, request):
        # print(request.POST.get('extra_field_count'))
        form = NewGameForm(request.POST)  ##, extra=request.POST.get('extra_field_count'))
        if not form.is_valid():
            print(f"Not valid")
            return render(request, 'game/createnewgame.html', {'form': form})
        print(form.cleaned_data.get('players'))
        users = form.cleaned_data.get('players')
        game_name = form.cleaned_data.get('name')

        new_game = Game.objects.create(name=game_name)
        new_game.save()
        for p in users:
            player = Player.objects.create(game=new_game, user=p)
            print(f"Add user {p} to game {new_game} as {player}")
            player.save()

        return HttpResponse(f"Invited users {', '.join([u.username for u in users])} for game: {new_game.name}")

class MyGamesView(View):

    def get(self, request):
        user = request.user
        player_exists = Player.objects.filter(user=user).exists()
        if not player_exists:
            return HttpResponse(f"No invites or games yet.")
        player = Player.objects.filter(user=user)
        print(player)
        games = []
        for p in player:
            # games_qs = Game.objects.filter(player=p)
            games.append(p.game)
        print(games)
        return render(request, 'game/my_games.html', {'invites': games, 'games': games})


# class NewGameView(View):
#     def get(self, request):
#         # Create new game
#         game = Game()
#         for u in User.objects.all():
#             player = Player()
#
#         return render(request, 'game/home.html')
