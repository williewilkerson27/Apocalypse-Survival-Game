

class Enemy:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def is_alive(self):
        return self.health > 0

class Todd(Enemy):
    def __init__(self, health=60, power=15):
        super().__init__('Todd', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'''
^^^^^^^ Todd just hit you with a metal pipe, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')
            
    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')


class Clarence(Enemy):
    def __init__(self, health=50, power=15):
        super().__init__('Clarence', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'''
^^^^^^^ Clarence just stabbed you with a broken glass bottle, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')

class John(Enemy):
    def __init__(self, health=40, power=10):
        super().__init__('John', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'''
^^^^^^^ John speared you with a sharpened Broom-Stick, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')
            

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')    


class Lachlan(Enemy):
    def __init__(self, health=50, power=20):
        super().__init__('Lachlan', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f'''
^^^^^^^ Lachlan took a shot at you with his rusty handgun, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')    


class Joey(Enemy):
    def __init__(self, health=40, power=10):
        super().__init__('Joey', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f''' 
^^^^^^^ Joey lit a firework, then threw it at you, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')


class Janine(Enemy):
    def __init__(self, health=40, power=10):
        super().__init__('Joey', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f''' 
^^^^^^^ Janine beat you with her old Windows laptop, - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')


class Rachel(Enemy):
    def __init__(self, health=40, power=15):
        super().__init__('Joey', power, health)
        self.power = power

    def attack(self, survivor):
        survivor.health -= self.power
        print(f''' 
^^^^^^^ Rachel hit you with a Hockey-Stick , - {self.power} HEALTH ^^^^^^^
''')
        if survivor.health <= 0:
            print('YOU ARE DEAD, Your Are Just A Memory Now!')

    def get_status(self):
        print(f'You have {self.health} and can do {self.power} power to another survivor')
