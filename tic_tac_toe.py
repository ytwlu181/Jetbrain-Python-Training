# project from https://hyperskill.org/curriculum
import random


class TicTacToe:

    def __init__(self):
        # using a 1d array to represent the initial board
        self.board =[0]*9 #0 means empty, 1 means X, -1 means O
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

    def judge_status(self):
        def update_winner(i):
            if self.board[i] == 1:
                self.winner =1
            elif self.board[i] == -1:
                self.winner = -1

        for i in range(3): #winner in one row
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                update_winner(i)

        for i in range(0, 7, 3): # winner in one column
            if self.board[i] == self.board[i + 1] == self.board[i + 2]:
                update_winner(i)

        if self.board[0] == self.board[4] == self.board[8]: #diagnol
            update_winner(0)

        if self.board[2] == self.board[4] == self.board[6]: #diagnol
            update_winner(2)

    def check_winner(self):
        count = sum([abs(self.board[i]) for i in range(9)])
        if self.winner != None:
            print(f'{self.convert[self.winner]} wins')
            self.stop_while()
        if count == 9 and self.winner == None:
            print("Draw")
            self.stop_while()


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

    # def

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

        # self.board_display()
        # while not self.terminate:
        #     self.user()
        #     self.check_winner()
        #     self.easy()
        #     self.check_winner()




new_game = TicTacToe()
new_game.main_loop()

