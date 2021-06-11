class Survivor:
    #damage is how much damage you inflict on your victim!
    def __init__(self, health=100, damage=20):
        self.health = health
        self.damage = damage

    def attack(self, other_survivor):
        other_survivor.health -= self.power
        print(f'You did {damage} Damage to {other_survivor}')
        if other_survivor.health <= 0:
            print(f'You killed {other_survivor}')

    def get_status(self):
        print(f'You have {self.health} and can do {self.damage} damage to another survivor')

    