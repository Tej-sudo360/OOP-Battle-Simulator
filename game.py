from goblin import Goblin


ARENA_NAME = "The Streets of Demopolis"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The Streets are opening...")

    goblin = Goblin("Richard")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    new_goblin = Goblin("jc")

    print(f"{new_goblin.name} enters the arena with {new_goblin.health} health.")


    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
