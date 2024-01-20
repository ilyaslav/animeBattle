class Hero:
    def __init__(self) -> None:
        self._power = 0
        self._intelligence = 0
        self._look = 0
        self.img = ""
        self._type = ""

    def __init__(self, power: int, intelligence: int, look: int, img : str, type_ : str) -> None:
        self._power = power
        self._intelligence = intelligence
        self._look = look
        self.img = img
        self._type = type_

    def get_type(self):
        return self._type

    @staticmethod
    def compare(h1, h2, param : str) -> bool:
        if param == 'power':
            return h1._power > h2._power
        elif param == 'intelligence':
            return h1._intelligence > h2._intelligence
        else:
            return h1._look > h2._look
