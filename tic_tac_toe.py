# project from https://hyperskill.org/curriculum
# minimax reference: https://github.com/Cledersonbc/tic-tac-toe-minimax
import random


class TicTacToe:

    def __init__(self):
        # using a 1d array to represent the initial board
        self.board =[0]*9 #0 means empty, 1 means X, -1 means O
        # self.board = [-1,-1,1,1,0,0,0,-1,1]
        self.terminate = False
        self.next_move = 1 # 1 to be replaced with X
        self.winner = None
        self.not_real_quit = True
        self.convert = {1:'X', -1:'O', 0:' '}

    def board_display(self):
        top_low_bound = "-" * 9
        print(top_low_bound)
        for key, value in enumerate(self.board):
            if key in {0,3,6}:
                print('| ' + str(self.convert[value]), end=' ')
            elif key in {2,5,8}:
                print(self.convert[value], end=' |\n')
            else:
                print(self.convert[value], end=' ')
        print(top_low_bound)

    def input_to_index(self,a, b):
        self.index = 8+a-3*b

    def if_format_wrong(self,user_input):
        t = user_input.split()
        digit_test = [i.isdigit() for i in t]
        if not all(digit_test):
            print("You should enter numbers!")
            return False
        if len(user_input.split()) != 2:
            print("Only input 2 numbers")
            return False
        a, b = user_input.split()
        a=int(a)
        b=int(b)
        if a<1 or a>3 or b<1 or b>3:
            print("Coordinates should be from 1 to 3!")
            return False

        self.input_to_index(a,b)

        if self.board[self.index] !=0:
            print("This cell is occupied! Choose another one!")
            return False
        return True

    def judge_status(self,copy_of_board = None):
        default_input = False
        winner = None
        if copy_of_board == None:
            copy_of_board = self.board
            default_input = True
        def update_winner(i):
            winner = None
            if copy_of_board[i] == 1:
                winner =1
            elif copy_of_board[i] == -1:
                winner = -1
            return winner

        for i in range(3): #winner in one column
            if copy_of_board[i] == copy_of_board[i+3] == copy_of_board[i+6] != 0:
                # print('here')
                winner = update_winner(i)

        for i in range(0, 7, 3): # winner in one row
            if copy_of_board[i] == copy_of_board[i + 1] == copy_of_board[i + 2] != 0:
                winner = update_winner(i)

        if copy_of_board[0] == copy_of_board[4] == copy_of_board[8] != 0: #diagnol
            winner = update_winner(0)

        if copy_of_board[2] == copy_of_board[4] == copy_of_board[6] != 0: #diagnol
            winner = update_winner(2)

        if default_input:
            self.winner = winner
        return winner

    def check_winner(self):
        count = sum([abs(self.board[i]) for i in range(9)])
        if self.winner != None:
            print(f'{self.convert[self.winner]} wins')
            self.stop_while()
        if count == 9 and self.winner == None:
            print("Draw")
            self.stop_while()

    def check_winner_copy(self,board_copy,winner):
        count = sum([abs(board_copy[i]) for i in range(9)])
        if winner != None:
            return winner
        if count == 9 and winner == None:
            return 0

    def stop_while(self):
        self.terminate = True

    def update_coor(self):
        i = self.index
        self.board[i] = self.next_move
        self.next_move = -self.next_move
        self.judge_status()

    def human_input(self):
        user_input = input("Enter the coordinates: ")
        while not self.if_format_wrong(user_input):
            user_input = input("Enter the coordinates: ")

    def get_board_copy(self):
        board_copy = []
        for i in self.board:
            board_copy.append(i)
        return board_copy

    def medium_move_decision(self,indices_0):
        for i in indices_0:
            board_copy = self.get_board_copy()
            board_copy[i] = self.next_move
            winner = self.judge_status(board_copy)
            if winner == self.next_move:
                return i

        for i in indices_0:
            board_copy = self.get_board_copy()
            board_copy[i] = -self.next_move
            winner = self.judge_status(board_copy)
            if winner == -self.next_move:
                return i
        return -1

    def medium(self):
        indices_0 = [i for i, j in enumerate(self.board) if j == 0]
        AI_new_move = self.medium_move_decision(indices_0)
        if AI_new_move == -1:
            AI_new_move = random.choice(indices_0)
        self.board[AI_new_move] =self.next_move
        self.next_move = -self.next_move
        print('Making move level "medium"')
        self.board_display()
        self.judge_status()
        self.check_winner()

    def hard(self):
        board_copy = self.get_board_copy()
        [m,AI_new_move] = self.minimax(board_copy, self.next_move)


        self.board[AI_new_move] = self.next_move
        self.next_move = -self.next_move
        print('Making move level "hard"')
        self.board_display()
        self.judge_status()
        self.check_winner()



    def minimax(self, board_copy, player):
        # return values:
        # 1st value: 1 or -1, indicate min or max
        # 2nd value: best move
        if player ==  self.next_move:
            best =  [-999, -1]
        else:
            best =  [999, -1]

        winner = self.judge_status(copy_of_board=board_copy)
        winner = self.check_winner_copy(board_copy, winner)

        if winner == self.next_move:
            return [1, -1]
        elif winner == -self.next_move:
            return [-1,-1]
        elif winner == 0:
            return [0,-1]

        indices_0 = [i for i, j in enumerate(board_copy) if j == 0]
        for i in indices_0:
            board_copy[i] = player
            score = self.minimax(board_copy,-player)
            board_copy[i] = 0
            score[1] = i
            if player == self.next_move:
                if score[0]>best[0]:
                    best = score
            else:
                if score[0]<best[0]:
                    best = score
        return best







    def easy(self):
        indices = [i for i, j in enumerate(self.board) if j == 0]
        AI_new_move = random.choice(indices)
        self.board[AI_new_move] =self.next_move
        self.next_move = -self.next_move
        print('Making move level "easy"')
        self.board_display()
        self.judge_status()
        self.check_winner()

    def user(self):
        self.human_input()
        self.update_coor()
        self.board_display()
        self.check_winner()

    def start_menu(self):
        start_input = input("Input command: ")
        while self.start_input_format_wrong(start_input):
            start_input = input("Input command: ")
        _,b,c = start_input.split()

        func_b = 'self.'+b+'()'
        func_c = 'self.'+c+'()'
        # print(func_b)
        self.board_display()
        while not self.terminate:
            eval(func_b)
            if self.terminate == True:
                break
            eval(func_c)



    def start_input_format_wrong(self,start_input):
        if start_input == "exit":
            quit()
        if len(start_input.split())!=3:
            return True
        a,b,c = start_input.split()
        if a != 'start':
            return True
        return False


    def main_loop(self):
        while self.not_real_quit:
            self.__init__()
            self.start_menu()



new_game = TicTacToe()
new_game.main_loop()

