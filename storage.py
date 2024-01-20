import random
from hero import Hero
from player import Player

class PlayerBox:
    def __init__(self) -> None:
        self.players = []

    def add_player(self, pl: Player):
        self.players.append(pl)

    def get_player(self, id : int):
        return self.players[id]


class HeroesBox:
    def __init__(self) -> None:
        self.heroes = [
            Hero(10, 100, 90, '', 'legendary'),
            Hero(13, 35, 64, '', 'common'),
            Hero(51, 26, 49, '', 'common'),
            Hero(42, 12, 58, '', 'common'),
            Hero(80, 50, 100, '', 'legendary'),
            Hero(71, 7, 36, '', 'common'),
            Hero(51, 54, 48, '', 'common'),
            Hero(72, 72, 67, '', 'rare'),
            Hero(0, 35, 50, '', 'common'),
            Hero(15, 26, 55, '', 'common'),
            Hero(50, 10, 66, '', 'common'),
            Hero(80, 80, 80, '', 'legendary'),
            Hero(91, 0, 80, '', 'rare'),
            Hero(12, 28, 60, '', 'common'),
            Hero(45, 94, 84, '', 'rare'),
            Hero(73, 28, 35, '', 'common'),
            Hero(100, 30, 90, '', 'legendary'),
            Hero(84, 75, 74, '', 'rare'),
            Hero(50, 25, 20, '', 'common'),
            Hero(75, 74, 66, '', 'rare'),
            Hero(61, 37, 41, '', 'common'),
            Hero(23, 65, 53, '', 'common'),
            Hero(95, 25, 61, '', 'rare'),
            Hero(83, 21, 92, '', 'rare'),
            Hero(73, 63, 76, '', 'rare'),
            Hero(29, 47, 52, '', 'common'),
            Hero(85, 63, 61, '', 'common'),
            Hero(14, 55, 47,'', 'common')
        ]

        self.l_heroes = []
        self.r_heroes = []
        self.c_heroes = []
        for hero in self.heroes:
            if hero.get_type() == 'legendary':
                self.l_heroes.append(hero)
            elif hero.get_type() == 'rare':
                self.r_heroes.append(hero)
            else:
                self.c_heroes.append(hero)

    def get_hero(self, id : int):
        return self.heroes[id]

    def get_legendary(self):
        hero = random.choice(self.l_heroes)
        return self.heroes.index(hero)

    def get_rare(self):
        hero = random.choice(self.r_heroes)
        return self.heroes.index(hero)

    def get_common(self):
        hero = random.choice(self.c_heroes)
        return self.heroes.index(hero)

hb = HeroesBox()
pb = PlayerBox()
