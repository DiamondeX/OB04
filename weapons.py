from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"