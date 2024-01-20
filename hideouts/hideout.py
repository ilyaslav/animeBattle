class Hideout:
    def __init__(self, type_ : str, rarity : str, position : int, player : int) -> None:
        self._type = type_
        self._rarity = rarity
        self._position = position
        self._player = player

    def action(self):
        pass
    def occupy(self):
        pass
