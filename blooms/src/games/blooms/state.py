from copy import deepcopy

from colorama import Fore

from src.games.blooms.action import BloomsAction
from src.games.state import State
# from src.games.blooms.players.human import HumanConnect4Player
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)


class BloomsState(State):
    EMPTY_CELL = -1

    def __init__(self):
        super().__init__()

        # management board
        self.board_01 = [[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                         [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]]

        # interface board
        self.board_x = [["-", "-", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-", "-"],
                        ["-", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-"],
                        ["-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-"],
                        [" ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " "],
                        ["-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-"],
                        ["-", "-", " ", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-"],
                        ["-", "-", "-", " ", "-", " ", "-", " ", "-", " ", "-", "-", "-"]]

        # if num_rows < 4:
        # raise Exception("the number of rows must be 4 or over")
        # if num_cols < 4:
        # raise Exception("the number of cols must be 4 or over")

        """
        the dimensions of the board
        """
        # self.__num_rows = num_rows
        # self.__num_cols = num_cols

        """
        the grid
        """
        # self.__grid = [[Connect4State.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

        self.__score = [0, 0]

    """
    def __check_winner(self, player):
        # check for 4 across
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row][col + 1] == player and \
                        self.__grid[row][col + 2] == player and \
                        self.__grid[row][col + 3] == player:
                    return True

        # check for 4 up and down
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col] == player and \
                        self.__grid[row + 2][col] == player and \
                        self.__grid[row + 3][col] == player:
                    return True

        # check upward diagonal
        for row in range(3, self.__num_rows):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__num_rows - 3):
            for col in range(0, self.__num_cols - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False
    """

    """
    def check_neighbor(self, x, y):
        hex_directions = [(0, -2), (-1, -1), (0, 2), (-1, 1), (1, 1), (1, -1)]
        for list_item in hex_directions:
            g = x + list_item[0]
            z = y + list_item[1]
            if self.board_01[g][z] == 0:
                # print("error, out of limits")
                continue
            if self.board_01[x][y] == 2 or self.board_01[x][y] == 3:
                if self.board_01[g][z] == 2 or self.board_01[g][z] == 3:
                    print("colors - 2/3")
                    print(f"({g},{z})")
                    print(self.board_01[g][z])
            if self.board_01[x][y] == 4 or self.board_01[x][y] == 5:
                if self.board_01[g][z] == 5 or self.board_01[g][z] == 5:
                    print("colors - 4/5")
                    print(f"({g},{z})")
                    print(self.board_01[g][z])
            # print(f"({g},{z})")
            # print(self.board_01[g][z])
    """

    # print management board
    def print_board_x(self):
        n = 0
        print('  0 1 2 3 4 5 6 7 8 9 10 11 12')
        for r in self.board_x:
            print(n, end=' ')
            n = n + 1
            for c in r:
                print(c, end=" ")
            print()

    def print_board_x_v1(self):
        n = 0
        print('  0 1 2 3 4 5 6 7 8 9|10|11|12')
        for r in self.board_x:
            print(n, end='')
            n = n + 1
            hexanterior = 1
            for c in r:
                if c == '-':
                    if hexanterior == 1:
                        print(r'  ', end='')
                        hexanterior = 1
                    continue
                else:

                    print(fr'{Fore.RED}/{Fore.BLUE}{c}{Fore.RED}\ ', end='')
                    hexanterior = 0
            print()
            # print(c, end=" ")
            hexanterior = 1
            print(' ', end='')
            for c in r:
                if c == '-':
                    if hexanterior == 1:
                        print(r'  ', end='')
                        hexanterior = 1
                    continue
                else:
                    print(Fore.RED + r'_/ ', end='')
                    hexanterior = 0
            print()

    # print interface board
    def print_board_01(self):
        for r in self.board_01:
            for c in r:
                print(c, end=" ")
            print()

    def get_board_01(self):
        return self.board_01

    def get_board_x(self):
        return self.board_x

    def get_num_players(self):
        return 2

    def validate_action(self, action: BloomsAction) -> bool:
        pos = action
        x = pos.get_x()
        y = pos.get_y()

        if self.board_01[x][y] != 1:
            # print("can't play there")
            return False

        return True

    def update(self, action: BloomsAction):
        # col = action.get_col()
        x = action.get_x()
        y = action.get_y()
        color = action.get_c()

        """
        # colors for player 0
        color_selected1 = 0
        # while color_selected1 != 1 and color_selected1 != 2:
        if self.get_acting_player() == 0:
            while color_selected1 != 1 and color_selected1 != 2:
                print("[1] color blue - id: 2")
                print("[2] color red - id: 3")
                color_selected1 = int(input("select the color: "))
                if color_selected1 == 1:
                    self.board_x[x][y] = "b"
                    self.board_01[x][y] = 2
                else:
                    self.board_x[x][y] = "r"
                    self.board_01[x][y] = 3

        # colors for player 1
        color_selected2 = 0
        if self.get_acting_player() == 1:
            while color_selected2 != 1 and color_selected2 != 2:
                print("[1] color green - id: 4")
                print("[2] color yellow - id: 5")
                color_selected2 = int(input("select the color: "))
                if color_selected2 == 1:
                    self.board_x[x][y] = "g"
                    self.board_01[x][y] = 4
                if color_selected2 == 2:
                    self.board_x[x][y] = "y"
                    self.board_01[x][y] = 5
        """

        if color == 2:
            self.board_x[x][y] = "b"
            self.board_01[x][y] = 2
        if color == 3:
            self.board_x[x][y] = "r"
            self.board_01[x][y] = 3
        if color == 4:
            self.board_x[x][y] = "g"
            self.board_01[x][y] = 4
        if color == 5:
            self.board_x[x][y] = "y"
            self.board_01[x][y] = 5

        # pelo que entendi... isso dá get da coluna que o player selecionou para jogar
        # e dá update o board...e define essa coluna como jogada pelo player
        # drop the checker
        """
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__grid[row][col] < 0:
                self.__grid[row][col] = self.__player_to_play
                break
        """
        # self.check_neighbor(action.get_x(), action.get_y())
        self.eat_after_play()

        self.__has_winner = self.check_winner(self.__acting_player)

        num = action.get_num()
        x1 = action.get_x1()
        y1 = action.get_y1()
        if num == 1:
            self.__acting_player = 1 if self.__acting_player == 0 else 0
            self.__turns_count += 1
        if num == 2:
            if self.__acting_player == 0:
                if color == 2:
                   self.board_x[x1][y1] = "r"
                   self.board_01[x1][y1] = 3
                if color == 3:
                   self.board_x[x1][y1] = "b"
                   self.board_01[x1][y1] = 2
            if self.__acting_player == 1:
                if color == 4:
                    self.board_x[x1][y1] = "y"
                    self.board_01[x1][y1] = 5
                if color == 5:
                    self.board_x[x1][y1] = "g"
                    self.board_01[x1][y1] = 4
            self.__acting_player = 0 if self.__acting_player == 1 else 1
            self.__turns_count += 2

        # print(self.__player_to_play)

        # determine if there is a winner
        # IMPLEMENTAR
        # self.__has_winner = self.check_winner(self.__acting_player)
        # switch to next player
        # self.__acting_player = 1 if self.__acting_player == 0 else 0
        # self.__turns_count += 1

        # self.__has_winner = self.check_winner(self.__acting_player)

    """
    def __display_cell(self, row, col):
        print({
            0:                              '\033[91mR\033[0m',
            1:                              '\033[94mB\033[0m',
            Connect4State.EMPTY_CELL:       ' '
        }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")
    """

    def __is_full(self) -> bool:
        count = 0
        for row in self.board_01:
            for col in row:
                if col == 1:
                    count = count + 1
        if count == 0:
            return True
        return False

    def is_finished(self) -> bool:
        if self.__has_winner or self.__is_full():
            return True

        return False

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        return deepcopy(self)

    """
    def get_result(self, pos) -> Optional[Connect4Result]:
        if self.__has_winner:
            return Connect4Result.LOOSE if pos == self.__acting_player else Connect4Result.WIN
        if self.__is_full():
            return Connect4Result.DRAW
        return None
    """

    """
    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols
    """

    def display(self):
        self.print_board_x()

    def get_result(self, pos):
        pass

    def before_results(self):
        pass

    def adj_to_position(self, row_idx, col_idx):
        hex_directions = [(0, -2), (-1, -1), (0, 2), (-1, 1), (1, 1), (1, -1)]

        v = []
        # adjacentes
        for direction in hex_directions:
            x = row_idx + direction[0]
            y = col_idx + direction[1]

            # print('::', x, y)

            # verificar cantos (se sair dos campos ignora)
            if 0 > x or x >= len(self.board_x) or 0 > y or y >= len(self.board_x[row_idx]):
                continue

            cell = self.board_01[x][y]
            if cell != 0:
                v.append(cell)

        return v

    # def _check_adj_positios_same_color(self, color: int, v: list):
        # flag = True
        # if flag is False:
        #    return 0
        # for pos in v:
        #    if color == self.board_01[pos.get_x][pos.get_y]:
        #        flag = True
        # while flag is True:
        # flag = self._check_adj_positions(color, v)
        # count = 0
        # while flag is False:
        #    count = count + 1
        #    print(count)

    def _check_adj_positions(self, color: int, v: list):
        has_to_be = (4, 5) if color in (2, 3) else (2, 3)

        pos1 = v.pop(0)

        # verificar se sao iguais
        flag = True
        for pos in v:
            if pos != pos1:
                flag = False
                break

        if flag is False:
            return False

        if pos1 not in has_to_be:
            return False

        return True

    def eat_after_play(self):
        # num = 0
        # score = 0
        count = 0

        # row
        for row_idx in range(len(self.board_x)):
            # col
            for col_idx in range(len(self.board_x[row_idx])):

                # ignora se campo for igual a 0
                if self.board_01[row_idx][col_idx] == 0:
                    continue

                color = self.board_01[row_idx][col_idx]
                adjs = self.adj_to_position(row_idx, col_idx)
                # print(row_idx, col_idx, color, adjs)

                if self._check_adj_positions(color, adjs):
                    self.print_stats(row_idx, col_idx)
                    self.board_01[row_idx][col_idx] = 1
                    self.board_x[row_idx][col_idx] = ""

    def print_stats(self, x, y):
        # count = 0

        if self.board_01[x][y] == 2 or self.board_01[x][y] == 3:
            self.__score[1] = self.__score[1] + 1
            # self.__score[1] = count
            print("\nPlayer ", 1, " - ", self.__score[1], "/", 20)

        if self.board_01[x][y] == 4 or self.board_01[x][y] == 5:
            self.__score[0] = self.__score[0] + 1
            # self.__score[0] = count
            print("\nPlayer ", 0, " - ", self.__score[0], "/", 20)

        # print("\nPlayer ", self.__acting_player, " - ", count, "/", 20)
        # return count

    def check_winner(self, player):
        if player == 0:
            if self.__score[0] >= 20:
                print("Player 0 win")
                return True
        if player == 1:
            if self.__score[1] >= 20:
                print("Player 1 win")
                return True
        return False