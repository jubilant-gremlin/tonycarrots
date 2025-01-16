from player import *
from room import *
from character import *
from item import *

class Game():
    def __init__(self):
        self.name = "GAME"

    def status(self):
        print(self.name + " IS INSTANTIATED")

    def grid(self, player):
        print("INSTANTIATE GRID")

        rooms = [start_room, cole_farm]

        for room in rooms:
            if player.pos_x == room.pos_x and player.pos_y == room.pos_y:
                room.status()

    def options(self, player):
        print("MOVE: (W), (A), (S), (D)")
        # PLAYER USER INPUT
        user_input = player.user_input()

        if user_input == "W":
            player.pos_y += 1
        elif user_input == "A":
            player.pos_x -= 1
        elif user_input == "S":
            player.pos_y -= 1
        elif user_input == "D":
            player.pos_x += 1
        else:
            print("INVALID CHOICE")
        return

    def main_loop(self, player):
        self.status()
        player.create()
        while True:
            self.grid(player)
            player.status()
            self.options(player)


# INSTANCE GAME
game = Game()

# RUN GAME MAIN LOOP
game.main_loop(player)
