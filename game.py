from goblin import Goblin
from hero import Hero

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




def main():
    """Open the arena and introduce its first opponent."""


    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The Streets are opening...")

    goblin = Goblin("Richard")
    

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    hedo = Hero("Mitchell")


    battle(hedo,goblin)



if __name__ == "__main__":
    main()
