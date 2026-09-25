import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name,100)
        self.attack_power = 15
        self.gold = 0


    def stealGold(self, hero):
        """Return True while the goblin has health remaining."""
        hero.gold = 0
        print("GET WRECKED NERD")
