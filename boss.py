import random
from enemy import Enemy

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name,300)
        self.attack_power = 30
        self.superMove = self.attack_power * 2


    def superMove(self, hero):
        """Return True while the Boss has health remaining."""
        hero.health = hero.health - self.superMove
        print("GET WRECKED NERD")