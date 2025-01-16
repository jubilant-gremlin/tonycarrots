import random

from item import *


class Character():
    def __init__(self, name, pos_x, pos_y, max_hp, i, st, dex, gp, xp, items,
                 weapons, armors, dialog):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.i = i
        self.st = st
        self.dex = dex
        self.gp = gp
        self.xp = xp
        self.items = items
        self.weapons = weapons
        self.armors = armors
        if self.weapons == []:
            self.dmg = 0
        else:
            self.dmg = self.weapons[0].dmg_value
        if self.armors == []:
            self.ar = 0
        else:
            self.ar = self.armors[0].ar_value
        self.dialog = dialog

    def status(self):
        print(self.name)
        print(f"{self.name} POS X: {self.pos_x}")
        print(f"{self.name} POS Y: {self.pos_y}")
        print(f"HP: {self.hp}")
        print(f"STR: {self.st}")
        print(f"DEX: {self.dex}")
        print(f"DMG: {self.dmg}")
        print(f"AR: {self.ar}")
        print(f"GP: {self.gp}")
        print(f"XP: {self.xp}")

        print("ITEMS:")
        for item in self.items:
            print(item.name)
        print("WEAPONS:")
        for weapon in self.weapons:
            print(weapon.name)
        print("ARMORS:")
        for armor in self.armors:
            print(armor.name)

    def roll_die(self, die):
        roll = random.randint(0, die)
        print(f"{self.name} ROLLS: {roll}")
        return roll


# INSTANTIATE CHARACTER    name, pos_x, pos_y, max_hp, i, st, dex, gp, xp, items, weapons, armor

farmer_cole = Character("FARMER COLE", 0, 0, 5, 15, 20, 15, 50, 20, [carrot], [], [cute_hat, little_shoes], "FOR THE LAST TIME TONY, I DON'T HAVE THOSE CARROTS")
tony_carrots = Character("TONY CARROTS", 0, 0, 1000, 1000, 1000, 1000, 1000, 1000, [], [], [], "EXCUSE ME, ARE YOU HERE TO HELP COLLECT CARROTS?")
