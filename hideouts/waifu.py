import sys
sys.path.insert(0, "..\\")

from hideout import Hideout
from storage import hb
from storage import pb
from hero import Hero
from player import Player

class Waifu(Hideout):
    def __init__(self, type_: str, rarity: str, position: int, player : int) -> None:
        super().__init__(type_, rarity, position, player)

    def occupy(self):
        player = pb.get_player(self._player)
        if player.get_heroes() < 4:
            if self._rarity == 'legendary':
                hero = hb.get_legendary()
            elif self._rarity == 'rare':
                hero = hb.get_rare()
            else:
                hero = hb.get_common()
            player.add_hero(hero)
