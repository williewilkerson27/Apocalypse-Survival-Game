class Character:
    def __init__(self, health):
        self.health = health

    def is_alive(self):
        return self.health > 0