import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Pegathon                   |
# Tiegan Cozzie      |
# Last Modified: November 30, 2021        |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# ---------------------------------------
# Start of Pegathon Class               |
# ---------------------------------------

class Pegathon:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    # Checks to see if there still is a possible legal move on the board
    def game_over(self):
        #the first two for loops go through the entire board
        for row_start in range(self.board.shape[0]):
            for col_start in range(self.board.shape[1]):
                # If the first two loops find a "True" it will pass through this if statement
                if self.board[row_start,col_start]:
                    # Goes through the whole board a second time for possible landing spots for selected peg
                    for row_end in range(self.board.shape[0]):
                        for col_end in range(self.board.shape[1]):
                            # If the move sent through legal_move is true game is not over
                            if self.legal_move(row_start,col_start,row_end,col_end):
                                return False
        return True
                                
        
        
    # Checks how many pegs are left on the board and displays proper message
    def final_message(self):
        if(self.pegs_left>=7):
            print("Number of pegs left: ",self.pegs_left)
            print("Peg-naramous! Rack 'em up and redeem yourself.")
        elif(self.pegs_left==5)or(self.pegs_left==6):
            print("Number of pegs left: ",self.pegs_left)
            print(self.pegs_left,"left? Really? You're gonna have to do better than that.")
        elif(self.pegs_left==3)or(self.pegs_left==4):
            print("Number of pegs left: ",self.pegs_left)
            print("I've worked with better. But not many.")
        elif(self.pegs_left<=2):
            print("Number of pegs left: ",self.pegs_left)
            print("You're a Peg-enius!")
                  
    # Checks to see if the move the user entered is possible
    def legal_move(self, row_start, col_start, row_end, col_end):
        if (self.board[row_start,col_start]==True):
            row_diff=row_start-row_end
            col_diff=col_start-col_end
            row_diff=abs(row_diff)
            col_diff=abs(col_diff)
            # The peg the user wants to move has to be within 2 columns and rows of the empty space
            if (row_diff<=2) and (col_diff<=2):
                # Checks to see if the space the user wants to land on doesn't have a peg 
                if(self.board[row_end,col_end]==False):
                    # Makes sure that the user cant move  peg that is illegal within the 2 by 2 box described 2 lines above
                    if(col_start!=col_end-1)and(row_start!=row_end-1)and(col_start!=col_end+1)and(row_start!=row_end+1):
                        row_diff=row_start-row_end
                        col_diff=col_start-col_end
                        # LInes 105-128 makes sure that the user is jumping over a peg and not an empty space
                        if(row_diff==-2)and(col_diff==2):
                            if self.board[row_start+1,col_start-1]==True:
                                return True
                        elif(row_diff==-2)and(col_diff==0):
                            if self.board[row_start+1,col_start]==True:
                                return True
                        elif(row_diff==-2)and(col_diff==-2):
                            if self.board[row_start+1,col_start+1]==True:
                                return True
                        elif(row_diff==0)and(col_diff==-2):
                            if self.board[row_start,col_start+1]==True:
                                return True
                        elif(row_diff==2)and(col_diff==-2):
                            if self.board[row_start-1,col_start+1]==True:
                                return True
                        elif(row_diff==2)and(col_diff==0):
                            if self.board[row_start-1,col_start]==True:
                                return True
                        elif(row_diff==2)and(col_diff==2):
                            if self.board[row_start-1,col_start-1]==True:
                                return True
                        elif(row_diff==0)and(col_diff==2):
                            if self.board[row_start,col_start-1]==True:
                                return True
            else:
                return False
        else:
            return False
            
    # Makes inputed move by user happen
    def make_move(self, row_start, col_start, row_end, col_end):
        # Removes the selected peg
        self.board[row_start,col_start]=False
        # Places peg in desired location
        self.board[row_end,col_end]=True
        row_diff=row_start-row_end
        col_diff=col_start-col_end
        # Lines 143-158 removes the peg that the user jumps over
        if(row_diff==-2)and(col_diff==2):
            self.board[row_start+1,col_start-1]=False
        elif(row_diff==-2)and(col_diff==0):
            self.board[row_start+1,col_start]=False
        elif(row_diff==-2)and(col_diff==-2):
            self.board[row_start+1,col_start+1]=False
        elif(row_diff==0)and(col_diff==-2):
            self.board[row_start,col_start+1]=False
        elif(row_diff==2)and(col_diff==-2):
            self.board[row_start-1,col_start+1]=False
        elif(row_diff==2)and(col_diff==0):
            self.board[row_start-1,col_start]=False
        elif(row_diff==2)and(col_diff==2):
            self.board[row_start-1,col_start-1]=False
        elif(row_diff==0)and(col_diff==2):
            self.board[row_start,col_start-1]=False

        # Counts how many pegs are left on the board
        self.pegs_left=self.pegs_left-1
        

# ---------------------------------------
# End of Pegathon Class                 |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Pegathon!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = Pegathon(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
