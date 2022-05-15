from src.games.blooms.players.human import HumanBloomsPlayer
from src.games.blooms.players.random import RandomBloomsPlayer
from src.games.blooms.simulator import BloomsSimulator
from src.games.blooms.players.custom import CustomBloomsPlayer


def main():
    # sim = BloomsSimulator(
    #    HumanBloomsPlayer("Inês"),
    #    HumanBloomsPlayer("Gonçalo"),
    # )

    #
    sim = BloomsSimulator(
        HumanBloomsPlayer("Inês"),
        RandomBloomsPlayer("Random")
    )

    sim.init_game()
    sim.run_simulation()


if __name__ == "__main__":
    main()