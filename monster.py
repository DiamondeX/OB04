class Monster:
    def __init__(self, health=100):
        self.health = health

    def is_defeated(self):
        return self.health <= 0