import random
from item import *


class Player():
    def __init__(self):
        self.name = "PLAYER"
        self.title = "JUNIOR ASSISTANT DEBT COLLECTOR"
        self.pos_x = 0
        self.pos_y = 0
        self.max_hp = None
        self.hp = self.max_hp
        self.i = None
        self.st = None
        self.dex = None
        self.dmg = None
        self.items = []
        self.skills = []
        self.weapons = []
        self.armors = []

    def status(self):
        print(self.name)
        print(f"{self.name} POS X: {self.pos_x}")
        print(f"{self.name} POS Y: {self.pos_y}")
        print(f"HP: {self.hp}")
        print(f"INT: {self.i}")
        print(f"STR: {self.st}")
        print(f"DEX: {self.dex}")
        print(f"DMG: {self.dmg}")

        for item in self.items:
            print(item.name)
        for skill in self.skills:
            print(skill.name)
        for weapon in self.weapons:
            print(weapon.name)
        for armor in self.armors:
            print(armor.name)

    def user_input(self):
        user_input = input(">>> ").upper()
        return user_input

    def create(self):
        self.status()
        print("CREATE YOUR CHARACTER")
        print("(N)AME YOUR CHARACTER")
        print("(R)OLL YOUR STATS")
        print("(P)LAY GAME")

        user_input = self.user_input()

        if user_input == "N":
            print("WHAT IS YOUR NAME?")
            user_input = self.user_input()
            self.name = user_input
            self.create()

        elif user_input == "R":
            print("ROLLING STATS")
            print("")
            print("ROLLING HP")
            roll = self.roll_die(20)
            self.hp = roll
            print("ROLLING INT")
            roll = self.roll_die(100)
            self.i = roll
            print("ROLLING STR")
            roll = self.roll_die(100)
            self.st = roll
            print("ROLLING DEX")
            roll = self.roll_die(100)
            self.dex = roll

            self.create()
            return

        elif user_input == "P":
            if self.name is None or self.hp is None:
                print("FINISH MAKING YOUR CHARACTER TO CONTINUE")
                self.create()
            print("PLAY THE GAME")

        else:
            print("INVALID INPUT, SELECT N, R, P")

    def roll_die(self, die):
        roll = random.randint(0, die)
        print(f"{self.name} ROLLS: {roll}")
        return roll


player = Player()
player.create()
