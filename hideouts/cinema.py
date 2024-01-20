import sys
sys.path.insert(0, "..\\")

from hideout import Hideout
from storage import hb
from storage import pb
from hero import Hero
from player import Player

class Cinema(Hideout):
    def __init__(self, type_: str, rarity: str, position: int, player : int, anime : int, money : int, hero : int) -> None:
        super().__init__(type_, rarity, position, player)
        self._anime = anime
        self._money = money
        self._hero = hero

    def action(self):
        player = pb.get_player(self._player)
        if self.try_watch(player.take_money()):
            player.add_count(self._anime)

    def try_watch(self, money):
        return money > self._money

    def occupy(self, hero, player):
        h1 = hb.get_hero(hero)
        h2 = hb.get_hero(self._hero)
        if Hero.compare(h1, h2):
            self._player = player
