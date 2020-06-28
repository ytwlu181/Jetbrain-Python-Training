# project from https://hyperskill.org/curriculum
class TicTacToe:
    def __init__(self):
        # Using a tuple(key) to string(value) dict to represent board
        coordinates = []
        for i in range(3, 0, -1):
            for j in range(3):
                coordinates.append((i, j + 1))
        board = {}
        coor_to_index = {}
        for coor in coordinates:
            board[coor] = '_'
        for i, coor in enumerate(coordinates):
            coor_to_index[coor] = i
        self.O = -1
        self.X = 1
        self.board = board
        self.terminate = False
        self.next_move = 'O'
        self.game_status = [0] * 9
        self.coor_to_index = coor_to_index
        self.new_coor_x = 0
        self.new_coor_y = 0
        self.winner = 'none'
        # print(self.board)

    def update_status(self, single_update=False):
        if single_update:
            index = self.coor_to_index[(self.new_coor_x, self.new_coor_y)]
            self.game_status[index] = self.X if self.next_move == 'X' else self.O
        else:
            for i, key in enumerate(self.board):
                if (self.board[key] == 'X'):
                    self.game_status[i] = self.X
                elif (self.board[key] == 'O'):
                    self.game_status[i] = self.O

    def judge_status(self):
        for i in range(3):
            if self.game_status[i] == self.game_status[i + 3] == self.game_status[i + 6]:
                self.winner = 'X' if self.game_status[i] == self.X else 'O'
        for i in range(0, 7, 3):
            if self.game_status[i] == self.game_status[i + 1] == self.game_status[i + 2]:
                self.winner = 'X' if self.game_status[i] == self.X else 'O'

        print(self.winner)

    def board_display(self):  # drawing the board with updated board info
        top_low_bound = "-" * 9
        print(top_low_bound)
        for key, values in self.board.items():
            values = values.replace('_', ' ')
            if key[1] == 1:
                print('| ' + values, end=' ')
            elif key[1] == 2:
                print(values, end=' ')
            else:
                print(values, end=' |\n')
        print(top_low_bound)

    def stop_game(self):
        self.terminate = True

    def if_format_wrong(self, user_input):
        t = user_input.split()
        digit_test = [i.isdigit() for i in t]
        if not all(digit_test):
            print("You should enter numbers!")
            return False
        if len(user_input.split()) != 2:
            print("Only input 2 numbers")
            return False
        a, b = user_input.split()
        self.new_coor_x = int(a)
        self.new_coor_y = int(b)
        # print(f'x is {self.new_coor_x}, y is{self.new_coor_y}')
        if self.new_coor_x < 1 or self.new_coor_x > 3 or self.new_coor_y < 1 or self.new_coor_y > 3:
            print("Coordinates should be from 1 to 3!")
            return False

        return True

    def if_coor_exist(self):
        if self.board[(self.new_coor_x, self.new_coor_y)] != '_':
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def first_map_creation(self, map_setup):
        count_x, count_o = 0, 0
        for i, j in zip(range(9), self.board):
            if map_setup[i] == 'X':
                self.board[j] = 'X'
                count_x += 1
            if map_setup[i] == 'O':
                self.board[j] = 'O'
                count_o += 1
        self.update_status()
        self.next_move = 'X' if count_x == count_o else 'O'  # if true, then next move should be X

    def update_coor(self, coor):
        self.board[(self.new_coor_x, self.new_coor_y)] = self.next_move
        self.update_status(single_update=True)
        self.judge_status()
        self.next_move = 'X' if self.next_move == 'O' else 'O'

    def main_loop(self):
        map_setup = input("Enter cells: ")
        self.first_map_creation(map_setup)
        while not self.terminate:
            print(self.game_status)
            self.board_display()
            user_input = input("Enter the coordinates: ")
            while not self.if_format_wrong(user_input) or not self.if_coor_exist():
                user_input = input("Enter the coordinates: ")
            self.update_coor(user_input)

            if (user_input == '0'):
                self.stop_game()


new_game = TicTacToe()
new_game.main_loop()

# O_OOXXXX_

