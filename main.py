from fighter import Fighter
from monster import Monster
from weapons import Sword, Bow


def fight(fighter, monster):
    while not monster.is_defeated():
        if fighter.weapon:
            print(f"Боец {fighter.attack_monster()}.")
            monster.health -= 10  # Предположим, что любое оружие наносит 10 урона
        else:
            print("Боец не может атаковать.")
            break

    if monster.is_defeated():
        print("Монстр побежден!")


# Демонстрация работы
fighter = Fighter()
monster = Monster()

# Боец выбирает меч
fighter.change_weapon(Sword())
print("Боец выбирает меч.")
fight(fighter, monster)

# Создаем нового монстра для следующего боя
monster = Monster()

# Боец выбирает лук
fighter.change_weapon(Bow())
print("\nБоец выбирает лук.")
fight(fighter, monster)