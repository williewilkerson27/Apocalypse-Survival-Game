from survivor import Survivor
from other_survivors import Todd, Clarence, John, Lachlan, Joey
import random

"""

In this Apocalypse Survival, You will attempt to stay alive till the military 
comes to rescue you! Rumors are the evacuation will take 10 days or more.
Only travel at night because there are snipers in the city.
This is your story, Survive or be forgotten..

"""



def main():

    survivor = Survivor('Wilky')
    enemies = [
        Todd(),
        Clarence(),
        John(),
        Lachlan(),
        Joey(),
    ]
    
    day = 1

    while survivor.is_alive() and day <= 10:
        print()
        print(f'''
______________ It is Day {day} ______________''')
        print()
        survivor.get_status()
        hour = 0
        while hour < 12 and survivor.is_alive():
            print(f'There are {12 - hour} hours left in the day')
            print('~~~~~ What do you want to do? ~~~~~')
            print('1: Eat')
            print('2: Sleep')
            print('3: Guard till Night')
            user_input = int(input())
            if user_input == 1:
                survivor.eat_food()
                hour += 3
                # else:
                #     print('You Have No More Food!')
            elif user_input == 2:
                #todo fix bug: user can enter a 100 hrs
                # fix it where it cant be more than remaining hrs till night
                hours_to_sleep = int(input('How many hours do you want to sleep? '))
                survivor.get_sleep(hours_to_sleep)
                hour += hours_to_sleep
            elif user_input == 3:
                hour = 12
            else:
                print('You need to enter ')    
        print('''
================= It is now Nightfall =================
        ''')
        night_hour = 0
        #here we are still checking if survivor isalive
        while night_hour < 12 and survivor.is_alive():
            print(f'There are {12 - night_hour} hours left in the night')
            print('What will you like to do?')
            print('1: Go Scavenge')
            print('2: Guard your home')
            print('3: Go to sleep')
            user_input = int(input())
            #* Go Scavenge INPUT1 *#
            if user_input == 1:
                night_hour += 6
                ran_enemy = random.randint(1,3)
                if ran_enemy == 2:
                    ran_enemy = random.choice(enemies)
                    print(f'~~~~~ {ran_enemy.name} is attacking you!! ~~~~~')
                    #* ========== Fight Sequence ========== *#
                    while ran_enemy.is_alive():
                        print()
                        print(f'1: Fight ')
                        print('2: Try to end this peacefully ')
                        print('3: Run Away ')
                        print(': ',)
                        user_input = int(input())
                        if user_input == 1:
                            print('fight!')
                            ran_enemy.attack(survivor)
                            survivor.attack(ran_enemy)
                        elif user_input == 2:  
                            ran_enemy.attack(survivor)
                            print('~~~ When you tried to stop fighting, your enemy hit you again! ~~~')
                        elif user_input == 3:
                            survivor.lose_food(1)
                            print(f'''
~~ Your enemy stole some food off you while you were running away! ~~
''')
                night_hour += 2
                ran_food = random.randint(1,3)
                survivor.food += ran_food
                print(f'===== You found {ran_food} cans of tuna! =====')
            #* _______________________________SCAVENGE_________________________________*#

            #* __________________If you choose to GUARD, INPUT2_______________________ *#
            elif user_input == 2:
                night_hour += 2
                ran_enemy = random.randint(1,5)
                if ran_enemy == 3:
                    ran_enemy = random.choice(enemies)
                    print(f'~~~~~ {ran_enemy.name} is attacking you!! ~~~~~')
                    
                    #* ========== Fight Sequence ========== *#
                    while ran_enemy.is_alive() and survivor.is_alive():
                        print()
                        print('1: Fight ')
                        print('2: Try to end this Peacefully ')
                        print('3: Run Away ')
                        print(': ',)
                        user_input = int(input())
                        #* What happens when you fight
                        if user_input == 1:
                            print('fight!')
                            ran_enemy.attack(survivor)
                            survivor.attack(ran_enemy)
                        #* What happens when you decide not to fight
                        elif user_input == 2:
                            ran_enemy.attack(survivor)
                            print('~~~ When you tried to stop fighting, your enemy hit you again! ~~~')
                        #* When you run away your enemy steals 1 item of food
                        elif user_input == 3:
                            survivor.lose_food(1)
                            print(f'''
~~ Your enemy stole some food off you while you were running away! ~~
''')
                            break
                        night_hour += 2
    #*______________________Guard_______________________________________________________*#

    #* _______________If user decides to sleep during an apocolypse INPUT3______________*#
            elif user_input == 3:  
                print('Sleeping Zzz Zz')
                ran_food = random.randint(1,2)
                if ran_food == 1:
                    survivor.robbery
                    print('''
^^^^^^ While you were sleeping, someone broke in and stole some food...
You woke up and they stabbed you with a kitchen knife and took off!!! ^^^^^^
                    ''')
                night_hour = 12
                


        day += 1
    if day == 10:
        print('''
++++++++++++++++++++++++++++++++++++++++++++++++
    You can hear the Military Helicopters!!
    They landed and you got yourself a seat,
    You fly away to a near U.N base and they
    make you feel right at home.
You Survived, Left with Memorys... Mainly Bad Ones
++++++++++++++++++++++++++++++++++++++++++++++++
''')
    exit()

main()