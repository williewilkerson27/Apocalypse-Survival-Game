class Survivor:
    #damage is how much damage you inflict on your victim!
    def __init__(self, name, health=70, damage=20, food=2):
        self.name = name
        self.health = health
        self.damage = damage
        self.food = food
    def attack(self, other_survivor):
        other_survivor.health -= self.damage
        print(f'You did {self.damage} Damage to {other_survivor.name}')
        if other_survivor.health <= 0:
            print(f'=== You Savagely Murdered {other_survivor.name} ===')

    def get_status(self):
        print(f'You have {self.health} Health and can do {self.damage} damage with your weapon')

    def robbery(self, health, quantity):
        self.health -= 20
        self.food -= quantity

    def eat_food(self):
        if self.food > 0:
            if self.health >= 70:
                print('Your Full, No More Food!')
            else:
                self.food -= 1
                self.health += 8
                print(f'You ate some food, Your health is now {self.health}')
        else:
            print('___ You need to find food! ___')

    def add_food(self, quantity):
        self.food += quantity

    def lose_food(self, quantity):
        self.food -= quantity

    def get_sleep(self, hours_to_sleep):
        total_hours = hours_to_sleep
        total_hours <= 12
        if self.health >= 70:
            while hours_to_sleep > 0:
                self.health += 0
                hours_to_sleep -= 1
        elif self.health <= 70:
            while hours_to_sleep > 0:
                self.health += 2
                hours_to_sleep -= 1
        print(f'''
    You slept, {total_hours} total hours. Your health is now {self.health}
        ''')
        
    def is_alive(self):
        return self.health > 0

    

    
