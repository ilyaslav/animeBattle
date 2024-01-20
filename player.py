class Player:
    def __init__(self, name : str, count : int, money : int, heroes : list, user_id : int, photo : str) -> None:
        self._name = name
        self._count = count
        self._money = money
        self._heroes = heroes
        self._user_id = user_id
        self._photo = photo

    def get_name(self):
        return self._name
    def get_count(self):
        return self._count
    def get_money(self):
        return self._money
    def get_heroes(self):
        return len(self._heroes)
    def get_hero(self, id : int):
        return self._heroes[id]
    def get_heroes_list(self):
        return self._heroes
    def get_user_id(self):
        return self._user_id
    def get_photo(self):
        return self._photo

    def set_name(self, name : str):
        self._name = name
    def set_count(self, count : int):
        self._count = count
    def set_money(self, money : int):
        self.money = money
    def set_heroes(self, heroes : list):
        self._heroes = heroes
    def set_user_id(self, user_id : int):
        self._user_id = user_id
    def set_photo(self, photo : str):
        self._photo = photo

    def add_count(self, count : int):
        self._count+=count
    def take_count(self, count : int):
        self._count-=count
    def add_money(self, money : int):
        self._money+=money
    def take_money(self, money : int):
        self._money-=money
    def add_hero(self, hero : int):
        self._heroes.append(hero)
    def take_hero(self, id : int):
        return self._heroes.pop(id)
