# project from https://hyperskill.org/curriculum
import random


class TicTacToe:

    def __init__(self):
        # Using a tuple(key) to string(value) dict to represent board
        coordinates = []
        for i in range(3, 0, -1):
            for j in range(3):
                coordinates.append((j + 1, i))
        board = {}
        coor_to_index = {}
        for coor in coordinates:
            board[coor] = '_'
        for i, coor in enumerate(coordinates):
            coor_to_index[coor] = i
        self.status_O = -1
        self.status_X = 1
        self.board = board
        self.terminate = False
        self.human_draw_X = 'X'
        self.AI_draw_O = 'O'
        self.game_status = [0] * 9
        self.coor_to_index = coor_to_index
        self.human_new_x = 0
        self.human_new_y = 0
        self.winner = 'none'
        # print(self.board)

    def intial_and_huamn_update_status(self, single_update=False):
        if single_update:
            index = self.coor_to_index[(self.human_new_x, self.human_new_y)]
            self.game_status[index] = self.status_X if self.human_draw_X == 'X' else self.status_O

        else:
            for i, key in enumerate(self.board):
                if (self.board[key] == 'X'):
                    self.game_status[i] = self.status_X
                elif (self.board[key] == 'O'):
                    self.game_status[i] = self.status_O

    def judge_status(self):
        def update_winner(i):
            if self.game_status[i] == self.status_X:
                self.winner = 'X'
            elif self.game_status[i] == self.status_O:
                self.winner = 'O'

        for i in range(3):
            if self.game_status[i] == self.game_status[i + 3] == self.game_status[i + 6]:
                update_winner(i)

        for i in range(0, 7, 3):
            if self.game_status[i] == self.game_status[i + 1] == self.game_status[i + 2]:
                update_winner(i)

        if self.game_status[0] == self.game_status[4] == self.game_status[8]:
            update_winner(0)

        if self.game_status[2] == self.game_status[4] == self.game_status[6]:
            update_winner(2)

        count = sum([abs(self.game_status[i]) for i in range(9)])
        if count == 9 and self.winner == 'none':
            print("Draw")
            self.stop_game()
        if self.winner != 'none':
            print(f'{self.winner} wins')
            self.stop_game()

    def board_display(self):  # drawing the board with updated board info
        top_low_bound = "-" * 9
        print(top_low_bound)
        for key, values in self.board.items():
            values = values.replace('_', ' ')
            if key[0] == 1:
                print('| ' + values, end=' ')
            elif key[0] == 2:
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
        self.human_new_x = int(a)
        self.human_new_y = int(b)
        # print(f'x is {self.new_coor_x}, y is{self.new_coor_y}')
        if self.human_new_x < 1 or self.human_new_x > 3 or self.human_new_y < 1 or self.human_new_y > 3:
            print("Coordinates should be from 1 to 3!")
            return False

        return True

    def if_coor_exist(self):
        if self.board[(self.human_new_x, self.human_new_y)] != '_':
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def update_coor_human(self, coor):
        self.board[(self.human_new_x, self.human_new_y)] = self.human_draw_X
        self.intial_and_huamn_update_status(single_update=True)
        self.board_display()
        self.judge_status()

    def update_coor_pc(self):
        indices = [i for i, j in enumerate(self.game_status) if j == 0]
        AI_new_move = random.choice(indices)
        self.game_status[AI_new_move] = self.status_O
        self.board[list(self.board.keys())[AI_new_move]] = self.AI_draw_O
        print('Making move level "easy"')
        self.board_display()
        self.judge_status()

    def main_loop(self):
        self.board_display()
        while not self.terminate:
            user_input = input("Enter the coordinates: ")
            while not self.if_format_wrong(user_input) or not self.if_coor_exist():
                user_input = input("Enter the coordinates: ")
            self.update_coor_human(user_input)
            if self.terminate == True:
                break
            self.update_coor_pc()


            if (user_input == '0'):
                self.stop_game()


new_game = TicTacToe()
new_game.main_loop()
