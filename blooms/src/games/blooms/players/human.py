from src.games.blooms.action import BloomsAction
from src.games.blooms.player import BloomsPlayer
from src.games.blooms.state import BloomsState


class HumanBloomsPlayer(BloomsPlayer):
    def __init__(self, name: str):
        super().__init__(name)

    def get_action(self, state: BloomsState) -> BloomsAction:
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                x, y = input(f"Player {state.get_acting_player()}, choose a space (x,y): ").split(",")
                color = self.select_color(state)
                num = self.number_play(state)
                if num == 1:
                    return BloomsAction(int(x), int(y), int(color), int(num), 0, 0)
                if num == 2:
                    # x1, y1 = input(f"Player {state.get_acting_player()}, choose a space (x,y): ").split(",")
                    # if state.validate_action_coords(x1, y1) is False:
                    #    while state.validate_action_coords(x1, y1) is False:
                    x1, y1 = input(f"Player {state.get_acting_player()}, choose other space (x,y): ").split(",")
                    return BloomsAction(int(x1), int(y1), int(color), int(num), int(x1), int(y1))
            except Exception:
                continue

    def number_play(self, state: BloomsState):
        num = input("play one more time? (1 - no/2 - yes)")
        if int(num) == 1:
            return 1
            # self.__acting_player = 1 if self.__acting_player == 0 else 0
            # self.__turns_count += 1
        if int(num) == 2:
            return 2
            # if self.__acting_player == 0:
            #    if color == 2:
            #        self.board_x[x][y] = "r"
            #        self.board_01[x][y] = 3
            #    if color == 3:
            #        self.board_x[x][y] = "b"
            #        self.board_01[x][y] = 2
            # if self.__acting_player == 1:
            #    if color == 4:
            #        self.board_x[x][y] = "y"
            #        self.board_01[x][y] = 5
            #    if color == 5:
            #        self.board_x[x][y] = "g"
            #        self.board_01[x][y] = 4
            # self.__acting_player = 1 if self.__acting_player == 1 else 0
            # self.__turns_count += 2

    def select_color(self, state: BloomsState):
        # colors for player 0
        color_selected1 = 0
        if state.get_acting_player() == 0:
            while color_selected1 != 2 and color_selected1 != 3:
                print("blue - 2")
                print("red - 3")
                color_selected1 = int(input("select the color: "))
            return color_selected1

        # colors for player 1
        color_selected2 = 0
        if state.get_acting_player() == 1:
            while color_selected2 != 4 and color_selected2 != 5:
                print("green - 4")
                print("yellow - 5")
                color_selected2 = int(input("select the color: "))
            return color_selected2

        return 1

    def event_action(self, pos: int, action, new_state: BloomsState):
        # ignore
        pass

    def event_end_game(self, final_state: BloomsState):
        # ignore
        pass
