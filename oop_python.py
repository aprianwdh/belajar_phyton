import os
os.system("cls")


class Player:
    def __init__(self,health=100,energy=200) -> None:
        self.health = health
        self.energy = energy
        
    def attack(self, target, damage=1):
        self.energy -= damage
        target.health -= damage
        print(f'player menyerang {damage} damage:')
        print(f'sisa energy = {self.energy}')
        print(f'sisa hp Dragon = {target.health}')
        if target.is_attack(target=self):
            self.health -= target.damage
            print(f'player diserang dragon {target.damage} damage: ')
            print(f'sisa hp player = {self.health}')


class Monster:
    def __init__(self,health=100,damage=10) -> None:
        self.health = health #dinamis atau berubah ubah
        self.health_init = self.health #statis atau  tidak akan berubah
        self.damage = damage
    def is_attack(self,target):
        return self.health < self.health_init


#deklarasi variabel
player1 = Player(health=150,energy=150)
player2 = Player()
dragon = Monster(health=500,damage=80)

#aksi aksi
player1.attack(target=dragon,damage=100)
# player2.attack(target=dragon,damage=80)


