import random as ran

def Fight(fighter_1, fighter_2):
    turn = ran.randint(1, 2)
    if turn == 1:
        print(f"Первым атакует {fighter_1.name}!")
        a = fighter_1
        b = fighter_2
    if turn == 2:
        print(f"Первым атакует {fighter_2.name}!")
        a = fighter_2
        b = fighter_1
    while a.health >= 0 and b.health >= 0:
        print(f"{a.name} атакует и наносит {a.strike()}")
        b.health -= int(a.strike())
        if b.health <= 0:
            print(f"{a.name} побеждает!")
        else:
            print(f"{b.name} атакует и наносит {b.strike()}")
            a.health -= int(b.strike())
            if a.health <= 0:
                print(f"{b.name} побеждает!")
              
class Servant:
    
    def __init__(self, name, health, attack, strength):
        self.name = name
        self.health = health
        self.attack = attack
        self.strength = strength

    def introduce(self):
        print(f"Меня зовут {self.name}")
        
    def strike(self):
        strike_damage = ran.randint(1, self.attack) + self.strength
        return strike_damage
     
Spartak = Servant("Спартак", 30, 10, 4)
Arthur = Servant("Король Артур", 40, 8, 3)
Fight(Spartak, Arthur)
