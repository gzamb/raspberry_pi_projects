#!/usr/bin/env python
"""
Tic-Tac-Toe Class

author: gzamb
"""

# TODO: Create algorithm to check rather than hard code wins
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


class TicTacToe:
    def __init__(self):
        # Need to setup the board to be 3x3 grid
        # and default squares to its grid value.
        # Then define the two players and initialize
        # first player as the current one.
        self.board = [str(x) for x in range(1, 10)]
        self.player_one = 'X'
        self.player_two = 'O'
        self.current_player = self.player_one

    def can_move(self):
        move = False
        for square in self.board:
            if square == ' ':
                move = True
                break
        return move

    def check_win(self, player):
        win = False
        for test in wins:
            count = 0
            for squares in test:
                if self.board[squares] == player:
                    count += 1
            if count == 3:
                win = True
        return win

    def get_move(self):
        correct_number = False
        while correct_number is False:
            square = input('Square to place the ' + self.current_player + ': ')
            try:
                square = int(square)
            except (ValueError, KeyError, TypeError):
                square = -2
            square -= 1  # make input number match internal numbers
            if 0 <= square < 10:  # number in range
                if self.board[square] == ' ':  # if it is blank
                    self.board[square] = self.current_player
                    correct_number = True
                else:
                    print('Square already occupied')
            else:
                print('incorrect square number try again')

    def play(self):
        self.print_board()
        print('Tic-Tac-Toe')
        print('two players')

        while True:
            self.wipe_board()
            while not self.check_win(self.swap_player(self.current_player)) and self.can_move():
                self.get_move()
                self.print_board()
                self.current_player = self.swap_player(self.current_player)
            if self.check_win(self.swap_player(self.current_player)):
                print('Player', self.swap_player(self.current_player), 'wins... New Game')
            else:
                print('A draw. ... New game')

    def print_board(self):
        print()
        print('- - - - - - -')
        print('|', end=' ')
        for square in range(0, 9):
            print(self.board[square], '|', end=' ')
            if square == 2 or square == 5:
                print()
                print('- - - - - - -')
                print('|', end=' ')
        print()
        print('- - - - - - -')
        print()

    def swap_player(self, player):
        return self.player_two if (self.player_one == player) else self.player_one

    def wipe_board(self):
        self.board = [' ' for _ in self.board]


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
