from character import *

from item import *

class Room():
    def __init__(self, name, desc, pos_x, pos_y, npcs, enemies, items,
                 weapons, armors):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.npcs = npcs
        self.enemies = enemies
        self.items = items
        self.weapons = weapons
        self.armors = armors

    def status(self):
        print(self.name)
        print(self.desc)
        print(f"ROOM X: {self.pos_x}")
        print(f"ROOM Y: {self.pos_y}")
        print("YOU SEE:")
        for npc in self.npcs:
            print(npc.name)
        for enemy in self.enemies:
            print(enemy.name)
        for item in self.items:
            print(item.name)
        for weapon in self.weapons:
            print(weapon.name)
        for armor in self.armors:
            print(armor.name)


# INSTANTIATE ROOM    name, desc, pos_x, pos_y, npcs, enemies, items, weapons, armors

start_room = Room("START ROOM", "THIS IS THE STARTING ROOM", 0, 0, [tony_carrots],
              [], [], [], [])
cole_farm = Room("COLE FARM", "THIS IS THE COLE FARM", 0, 1, [farmer_cole],
             [], [], [], [])
