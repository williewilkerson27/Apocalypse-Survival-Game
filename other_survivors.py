from character_health import Character

class Enemy:
    def __init__(self, name, damage, health):
        

class Todd(Character):
    def __init__(self, health=60, damage=15):
        super().__init__(health)
        self.damage = damage

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'Gary just hit you with a metal pipe, {self.damage}- HEALTH')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')


class Clarence(Character):
    def __init__(self, health=50, damage=20):
        super().__init__(health)
        self.damage = damage

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'Clarence just stabbed you with a broken glass bottle, {self.damage}- HEALTH')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')

class John(Character):
    def __init__(self, health=40, damage=10):
        super().__init__(health)
        self.damage = damage

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'John speared you with a sharpened Broom-Stick, {self.damage}- HEALTH')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')    


class Lachlan(Character):
    def __init__(self, health=70, damage=20):
        super().__init__(health)
        self.damage = damage

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'Lachlan took a shot at you with his rusty handgun, {self.damage}- HEALTH')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')    


class Joey(Character):
    def __init__(self, health=40, damage=10):
        super().__init__(health)
        self.damage = damage

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'Joey lit a firework, then threw it at you, {self.damage}- HEALTH')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')


