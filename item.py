import random


class Item():
    def __init__(self, name, dmg_value, ar_value, gp_value, weight):
        self.name = name
        self.dmg_value = dmg_value
        self.ar_value = ar_value
        self.gp_value = gp_value
        self.weight = weight

    def status(self):
        print(self.name)
        print(f"DMG VALUE: {self.dmg_value}")
        print(f"AR VALUE: {self.ar_value}")
        print(f"GP VALUE: {self.gp_value}")
        print(f"WEIGHT: {self.gp_value}")


# INSTANCE ITEM    name, dmg_value, ar_value, gp_value, weight
# WEAPONS
poo = Item(
    "POO",
    random.randint(1, 4) * random.randint(1, 4),
    0,
    1,
    .1,
)
# ARMORS
cute_hat = Item("CUTE HAT", 0, 1, 20, 1)
little_shoes = Item("LITTLE SHOES", 0, 1, 20, 1)
# ITEMS
carrot = Item("CARROT", 0, 0, 100, 0)
