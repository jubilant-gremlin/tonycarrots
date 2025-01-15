class Room():
    def __init__(self, name, desc, pos_x, pos_y):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y

    def status(self):
        print(self.name)
        print(self.desc)
        print(f"ROOM X: {self.pos_x}")
        print(f"ROOM Y: {self.pos_y}")
