from goblin import Goblin
from hero import Hero
from boss import Boss

ARENA_NAME = "The Streets of Demopolis"

def battle(hero: Hero,enemy: Goblin):
    while hero.is_alive and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")


def battleBoss(hero :Hero,enemy: Boss):
    while hero.is_alive and Boss.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if hero.health < 100:
            hero.health = hero.health - enemy.superMove
            print(" Boss: YOU CANT STOP ME!!!")

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")
        


def main():
    """Open the arena and introduce its first opponent."""


    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The Streets are opening...")

    goblin = Goblin("Richard")
    boss = Boss("Aiden")
    hedo = Hero("Mitchell")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    battle(hedo,goblin)

    print(f"{boss.name} enters the arena with {boss.health} health.")
    battle(boss,hedo)





if __name__ == "__main__":
    main()
    
