 #Brittany Strong
#September 14, 2023
#Project #1 Minimax Tic Tac Toe game
#this project will create a minimax board game by creating a list of 3 and giving the list 3 places. Then we implement function to check if board is full/make sure board is empty, so that we can start the game. From there we can create functions like makeMove that will allow for the users move to be appended to the list and get move from ai which will append the algorithms move to the list.

import copy
import random
import math

# Set the min-max IDs, and pseudo infinity constants
MIN = -1
MAX = 1
INFINITY_POSITIVE = math.inf
INFINITY_NEGATIVE = -math.inf

#this class creates the Tic Tac Toe board by creating a list with two ranges of 3 and adding X to the identifying class, this way we know that the Computer will not use X
class TicTacToe:
    def __init__(self) -> None:
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("--------")
  #creates the valid moves on the board by finding when places in column are equal to each other
    def valid_move(self, row, column):
        return 0 <= row < 3 and 0 <= column < 3 and self.board[row][column] == ''

    def make_move(self, row, column):
        if self.valid_move(row, column):
            self.board[row][column] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            return True
        return False

    def is_board_full(self):
        return all(cell != '' for row in self.board for cell in row)

    def get_score_for_ai(self):
        # Checking scoring logic for the game
        for row in self.board:
            if row.count('X') == 3:
                return 1  # X wins, return a positive score
            elif row.count('O') == 3:
                return -1  # O wins, return a negative score

        for col in range(3):
            if all(self.board[row][col] == 'X' for row in range(3)):
                return 1
            elif all(self.board[row][col] == 'O' for row in range(3)):
                return -1

        if all(self.board[i][i] == 'X' for i in range(3)) or all(self.board[i][2 - i] == 'X' for i in range(3)):
            return 1
        elif all(self.board[i][i] == 'O' for i in range(3)) or all(self.board[i][2 - i] == 'O' for i in range(3)):
            return -1

        return 0  # No winner yet, return 0 for a tie


# Modified code from Grokking, the starting point in my code
#everything else is built to run with Move
class Move:
    def __init__(self, move=0, value=0):
        self.move = move
        self.value = value


# Choose a move given a game and a search depth
def choose_move(board, depth):
    print('Computer is Thinking...')
    return minmax(board, depth, MAX, 0).move


# Search using the minmax algorithm given a game, search depth, player's ID, and default move
def minmax(board, depth, min_or_max, move):
# changes to the code include calling to the board created and the index
    current_score = board.get_score_for_ai()
    current_is_board_full = board.is_board_full()
    # Return the default move if it doesn't make sense to search for one
    if current_score != 0 or current_is_board_full or depth == 0:
        return Move(move, current_score)
#gets negative best score for computer and the avaiable moves
    best_score = INFINITY_NEGATIVE * min_or_max
    best_max_move = -1
    available_moves = [(i, j) for i in range(3) for j in range(3) if board.valid_move(i, j)]

#
    for index, (row, column) in enumerate(available_moves):
        neighbor = copy.deepcopy(board)
        neighbor.make_move(row, column)
        best = minmax(neighbor, depth - 1, min_or_max * -1, index)
#gives new best score and index
        if (min_or_max == MAX and best.value > best_score) or (min_or_max == MIN and best.value < best_score):
            best_score = best.value
            best_max_move = index
#else let the player make a move 
    return Move(best_max_move, best_score)

#Drive Code
# Create board
board = TicTacToe()

# Print the initial empty board
board.display()

#while the board is being displayed
while True:
  #prompt user for inputs to row and column
    user_row = int(input("Enter the row (0, 1, 2): "))
    user_column = int(input("Enter the column (0, 1, 2): "))
  
  #if board is a valid move then user can make move, else check vacancy, check if valid
    if board.valid_move(user_row, user_column):
        board.make_move(user_row, user_column)
        board.display()

        if board.is_board_full():
            print("\nIt's a Tie!")
            break
#call to available moves,
        available_moves = [(i, j) for i in range(3) for j in range(3) if board.valid_move(i,j)]

      #if not in availabel moves print tie or the board is full
        if not available_moves:
            print("\nIt's a Tie!")
            break
        if board.is_board_full():
            print("\nIt's a Tie!")
            break
    # Check for a winner after each move
        winner = board.get_score_for_ai()
        if winner == 1:
            print("\nYou win!")
            break
        elif winner == -1:
            print("\nComputer wins!")
            break
        #gives choose_move a depth to work with
        computer_move = choose_move(board, 9)
      
        computer_row, computer_column = available_moves[computer_move]
        board.make_move(computer_row, computer_column)
        board.display()

        if board.is_board_full():
          print("\nIt's a Tie!")
          break
        else:
          print("Invalid move. Try again.")

