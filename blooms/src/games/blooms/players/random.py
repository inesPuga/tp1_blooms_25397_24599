from random import randint, randrange

from src.games.blooms.action import BloomsAction
from src.games.blooms.player import BloomsPlayer
from src.games.blooms.state import BloomsState
from src.games.state import State


class RandomBloomsPlayer(BloomsPlayer):

    def __init__(self, name):
        super().__init__(name)
        self.coord = [[0, 3], [0, 5], [0, 7], [0, 9],
                      [1, 2], [1, 4], [1, 6], [1, 8], [1, 10],
                      [2, 1], [2, 3], [2, 5], [2, 7], [2, 9], [2, 11],
                      [3, 0], [3, 2], [3, 4], [3, 6], [3, 8], [3, 10], [3, 12],
                      [4, 1], [4, 3], [4, 5], [4, 7], [4, 9], [4, 11],
                      [5, 2], [5, 4], [5, 6], [5, 8], [5, 10],
                      [6, 3], [6, 5], [6, 7], [6, 9]]

    def get_action(self, state: BloomsState):
        state.display()
        while True:
            try:
                pos_array = randrange(37)
                coord = self.coord[pos_array]
                pos_x = coord[0]
                # print(pos_x)
                pos_y = coord[1]
                # print(pos_y)
                print("\n")
                print(f"Player, {state.get_acting_player()}", "-", "(", pos_x, ",", pos_y, ")")
                color_bot_random = self.select_color(state)
                array = [1, 2]
                num = randrange(2)
                if array[num] == 1:
                    return BloomsAction(pos_x, pos_y, color_bot_random, array[num], 0, 0)
                if array[num] == 2:
                    # x1, y1 = input(f"Player {state.get_acting_player()}, choose a space (x,y): ").split(",")
                    pos_array = randrange(37)
                    coord = self.coord[pos_array]
                    pos_x1 = coord[0]
                    # print(pos_x)
                    pos_y1 = coord[1]
                    print(f"Player, {state.get_acting_player()}", "-", "(", pos_x1, ",", pos_y1, ")")
                    return BloomsAction(pos_x, pos_y, color_bot_random, array[num], pos_x1, pos_y1)
                # return Connect4Action(pos_x, pos_y, color_bot_random)
            except Exception:
                continue

    def select_color(self, state: BloomsState):
        # colors for player 0
        # color_selected1 = 0
        if state.get_acting_player() == 0:
            # while color_selected1 != 2 and color_selected1 != 3:
            array = [2, 3]
            pos_array = randrange(2)
            # print(array_c1[pos_array])
            color_selected1 = array[pos_array]
            return color_selected1

        # colors for player 1
        # color_selected2 = 0
        if state.get_acting_player() == 1:
            # while color_selected2 != 4 and color_selected2 != 5:
            array = [4, 5]
            pos_array = randrange(2)
            # print(array_c1[pos_array])
            color_selected2 = array[pos_array]
            return color_selected2

        return 1

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
