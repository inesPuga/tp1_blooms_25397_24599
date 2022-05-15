from src.games.blooms.player import BloomsPlayer
from src.games.blooms.state import BloomsState
from src.games.game_simulator import GameSimulator
from src.games.state import State


class BloomsSimulator(GameSimulator):

    def __init__(self, player1: BloomsPlayer, player2: BloomsPlayer):
        super(BloomsSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the blooms grid
        """
        # self.__num_rows = num_rows
        # self.__num_cols = num_cols

    """
    def init_game(self):
        return Connect4State(self.__num_rows, self.__num_cols)
    """

    def init_game(self) -> State:
        return BloomsState()

    def before_end_game(self, state: BloomsState):
        # ignored for this simulator
        pass

    def end_game(self, state: BloomsState):
        # ignored for this simulator
        pass
