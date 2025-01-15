class Player():
    def __init__(self):
        self.name = "PLAYER"
        self.pos_x = 0
        self.pos_y = 0

    def status(self):
        print(self.name)
        print(f"{self.name} POS X: {self.pos_x}")
        print(f"{self.name} POS Y: {self.pos_y}")

    def user_input(self):
        user_input = input(">>> ").upper()
        return user_input
    
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
