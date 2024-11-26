from weapons import Weapon

class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def attack_monster(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "не может атаковать, у него нет оружия"