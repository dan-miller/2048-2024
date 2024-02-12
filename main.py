"""
Abstraction Reference Guide:
    main                - responsible for starting the game and directing control to each function, the tests, or quitting
        board           - a variable within main that contains the current board and is passed to most functions as an argument
    System Functions:
        get_key_press   - returns the user's key_press input as an ascii value
        clear           - clears the screen (should be called before each print_board call)
        pause           - a function used by the GUI to allow for a slight delay that is more visually appealing in placing the new piece
    Board Functions:
        make_board      - creates a new, empty square board of N x N dimension
        print_board     - prints out the state of the argument board
        board_full      - returns True if the board is full and False otherwise
    Logic:
        swipe_right     - simulates a right swipe on the argument board
        swipe_left      - simulates a left swipe on the argument board
        swipe_up        - simulates a upward swipe on the argument board
        swipe_down      - simulates a downward swipe on the argument board
        swap            - occurs when the spacebar is pressed and randomly switches two different numbers on the board
        swap_possible   - a helper function that returns True if a swap is possible and False otherwise
    Useful Helper Functions:
        get_piece       - gets the piece from the given board at the given (x,y) coordinates or returns None if the position is invalid
        place_piece     - places the given piece on the given board at the given (x,y) coordinates and returns True or returns False if the position is invalid
        place_random    - user implemented function which places a random 2 OR 4 OR 8 in an empty part of the board
        have_lost       - responsible for determining if the game has been lost yet (no moves remain)
        move_possible   - responsible for determining if a move is possible from a single position
        move            - responsible for moving a piece, at the given (x,y) coordinates in the given direction on the given board
"""
# Global leaderboard variable, it's a global because reasons. Don't worry about it.
leaderboard = {}

def main():

    #Creating my new 4x4 board
    board = make_board(4)

    #Getting the game started with a single piece on the board
    place_random(board)
    print_board(board)

    #Runs the game loop until the user quits or the game is lost
    while True:

        #Gets the key pressed and stores it in the key variable
        #Hint: look at the available functions in the "Abstraction Reference Guide"
        #starting on line 2. You'll use those functions throughout the
        #project.
        key = ">>>>>>>>>>YOUR CODE HERE 2<<<<<<<<<<"

        #Quit case ('q')
        if ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            print("Bye bye!");
            quit()

        #Up arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Down arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Right arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Left arrow
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line) <<<<<"

        #Space bar (swap)
        elif ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<":
            "YOUR CODE HERE (1 line)"

        #Check to see if I've lost at the end of the game or not
        if ">>>>>>>>>>YOUR CODE HERE 4<<<<<<<<<<":

            # This will be zero until you complete the final steps of the project
            score = compute_score(board)
            input('Game over! Your score is ' + str(score) + '. Press enter to continue..')
            process_leaderboard(leaderboard, score)
            print_leaderboard(leaderboard)

            print("Would you like to play again? (y/n)");

            if (input() == 'y'):
                main();
            else:
                quit()

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def get_piece(x, y, board):
    """
    Utility function that gets the piece at a given (x,y) coordinate on the given board
    Returns the piece if the request was valid and None if the request was not valid
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to get the piece from
    """
    
    #Ensure that x and y are both integers (use assert)
    ">>>>>>>>>>YOUR CODE HERE 5<<<<<<<<<<"

    #What does this do?
    N = len(board)

    #Checking that the (x,y) coordinates given are valid for the N x N board
    ">>>>>>>>>>YOUR CODE HERE 6<<<<<<<<<<"

    #Getting the piece on the board
    return board[y][x]


def place_piece(piece, x, y, board):
    """
    Utility function that places the piece at a given (x,y) coordinate on the given board if possible
    Will overwrite the current value at (x,y), no matter what that piece is
    Returns True if the piece is placed successfully and False otherwise
    Arg piece: string - represents a piece on the board ('*' is an empty piece, '2' '8' etc. represent filled spots)
    Arg x: integer - x coordinate
    Arg y: integer - y coordinate
    Arg board: board - the board you wish to place the piece on
    """
    
    #Ensure that x and y are both integers (use assert)
    ">>>>>>>>>>YOUR CODE HERE 7<<<<<<<<<<"

    #What are the dimensions of the board?
    ">>>>>>>>>>YOUR CODE HERE 8<<<<<<<<<<"

    #Checking that the (x,y) coordinates given are valid for the board
    ">>>>>>>>>>YOUR CODE HERE 9<<<<<<<<<<"

    #Placing the piece on the board
    #Note how it's y (row), then x (column)
    board[y][x] = piece
    return True

#End of Step 1 #############################################################################################


#Start of Step 2 ###########################################################################################

def place_random(board):
    """
    Helper function which is necessary for the game to continue playing
    Returns True if a piece is placed and False if the board is full
    Places a 2 (60%) or 4 (37%) or 8 (3%) randomly on the board in an empty space
    Arg board: board - the board you wish to place the piece on
    """
    
    #Delete this return statement AND comment before beginning Step 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return;

    #Check if the board is full and return False if it is
    ">>>>>>>>>>YOUR CODE HERE 10<<<<<<<<<<"

    #random.random() generates a random decimal between [0, 1) ... Multiplying by 100 generates a number between [0, 100)
    generated = random.random() * 100;

    #Assign to_place according to my generated random number

    if generated < -1:                              #YOUR CODE HERE (replace -1) <<<<<
        to_place = "2"

    elif generated < -1 and generated >= -1:        #YOUR CODE HERE (replace -1) <<<<<
        to_place = "4"

    else:
        #What should to_place be if it's not a 2 or 4?
        to_place = ">>>>>>>>>>YOUR CODE HERE 11<<<<<<<<<<"


    #Variable keeps track of whether a randomly generated empty spot has been found yet
    found = False
    N = len(board)

    while not found:
        #Generate a random (x,y) coordinate that we can try to put our new value in at
        #How did we "generate" a random number earlier? (hint: x and y should be between [0, N) )
        random_y = ">>>>>>>>>>YOUR CODE HERE 12<<<<<<<<<<"
        random_x = ">>>>>>>>>>YOUR CODE HERE 13<<<<<<<<<<"

        #Think about why this is necessary ( hint: changes 3.4 (float) -> 3 (int) )
        random_y = int(random_y)
        random_x = int(random_x)

        #If the randomly generated coordinates are empty, we have found a spot to place our random piece
        found = get_piece(random_x, random_y, board) == '*'

    #Place the piece at the randomly generated (x,y) coordinate
    ">>>>>>>>>>YOUR CODE HERE 14<<<<<<<<<<"

    return True

#End of Step 2 #############################################################################################


#Start of Step 3 ###########################################################################################

def have_lost(board):
    """
    Helper function which checks at the end of each turn if the game has been lost
    Returns True if the board is full and no possible turns exist and False otherwise
    Arg board: board - the board you wish to check for a losing state
    """

    #Delete this return statement AND comment before beginning Step 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return False


    N = len(board)

    #Check every (x,y) position on the board to see if a move is possible
    for y in range(N):
        for x in range(N):
            ">>>>>>>>>>YOUR CODE HERE 15<<<<<<<<<< (1 or 2 lines)"

    return True

#End of Step 3 #############################################################################################


#Start of Step 4 ###########################################################################################

def end_move(board):
    """
    Prints the board after a swipe, pauses for .2 seconds, places a new random piece and prints the new state of the board
    Arg board: board - the board you're finishing a move on
    """
    
    #Print the board
    ">>>>>>>>>>YOUR CODE HERE 16<<<<<<<<<< (2 lines)"

    #Pause for .2 seconds
    ">>>>>>>>>>YOUR CODE HERE 17<<<<<<<<<<"

    #Place a random piece on the board at a random (x,y) position
    ">>>>>>>>>>YOUR CODE HERE 18<<<<<<<<<<"

    #Print the board again
    ">>>>>>>>>>YOUR CODE HERE 19<<<<<<<<<< (2 lines)"

#End of Step 4 #############################################################################################



#Start of Step 5 ###########################################################################################

def swipe_left(board):
    """
    YOUR COMMENT HERE (WHAT DOES THIS FUNCTION DO?)
    Arg board: board - (WHAT IS A BOARD ARGUMENT?)
    """
    
    #YOUR COMMENT HERE
    action_taken = False

    #YOUR COMMENT HERE
    N = len(board)

    #YOUR COMMENT HERE
    for y in range(N):
        for x in range(N):
            #YOUR COMMENT HERE
            piece_at_xy = get_piece(x, y, board)
            left_adjacent = get_piece(x-1, y, board)

            #YOUR COMMENT HERE
            if piece_at_xy == '*':
                continue

            #YOUR COMMENT HERE
            if left_adjacent == None:
                continue

            #YOUR COMMENT HERE
            action_taken = move(x, y, "left", board) or action_taken


    #YOUR COMMENT HERE
    if action_taken:
        end_move(board)

def swipe_right(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        for x in range(N):
            #Don't worry about why this is done (is not needed for up or left)
            x = N-1-x

            piece_at_xy = get_piece(x, y, board)
            right_adjacent = get_piece(x+1, y, board)

            if piece_at_xy == '*':
                continue

            if right_adjacent == None:
                continue

            action_taken = move(x, y, "right", board) or action_taken


    if action_taken:
        end_move(board)

def swipe_up(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        for x in range(N):
            piece_at_xy = get_piece(x, y, board)
            up_adjacent = get_piece(x, y-1, board)

            if piece_at_xy == '*':
                continue

            if up_adjacent == None:
                continue

            action_taken = move(x, y, "up", board) or action_taken


    if action_taken:
        end_move(board)

def swipe_down(board):
    action_taken = False

    N = len(board)

    for y in range(N):
        #Don't worry about why this is done (is not needed for up or left)
        y = N-1-y

        for x in range(N):

            piece_at_xy = get_piece(x, y, board)
            down_adjacent = get_piece(x, y+1, board)

            if piece_at_xy == '*':
                continue

            if down_adjacent == None:
                continue

            action_taken = move(x, y, "down", board) or action_taken


    if action_taken:
        end_move(board)

#End of Step 5 #############################################################################################


#Start of steps 6 and 7 ####################################################################################   - Section 3 -


def swap(board):
    """
    Note: have_lost does not take into account possible swaps that can "save the day". This is expected behavior.
    """
    N = len(board);

    #Check that a swap can occur on the board -- use the provided function, return False if a swap is not possible
    ">>>>>> YOUR CODE HERE (2 lines) <<<<<<"


    #Getting the first random piece to swap
    random_x1 = None
    random_x2 = None
    random_y1 = None
    random_y2 = None
    first_random_piece = None
    second_random_piece = None
    found = False;
    while not found:
        break # << delete this when you start

        # Pick a random x and y position within the board boundaires, store them in the
        # appropriate variables

        # Get the piece from that position and store it in the appropriate variable

        # If that piece is NOT "empty" (an asterisk), set found to True and store it

    # Do it again, with the second random piece
    found = False;
    while not found:
        break # << delete this when you start


    #Swap the first and second pieces using place piece and the random x/y values
    
    # print the board again
    clear()
    print_board(board)
    
    #An action was taken, so return true
    return True;


def swap_possible(board):
    """
    Helper function for swap
    Returns True if a swap is possible on the given board and False otherwise
    """
    
    # A set is like a list, but it can't have duplicate values
    container = set();
    N = len(board);
    
    for y in range(N):
        for x in range(N):
            piece_at_xy = get_piece(x, y, board);

            #Don't add empty spaces (they obviously can't be swapped...)
            #If the piece_at_xy is not empty... add it to the set using container.add(...)

    unique_pieces = len(container);

    # If there are fewer than 2 unique pieces, print "Can't swap" and return False, otherwise Return True
    pass


#End of steps 6 and 7 ######################################################################################

#Start of step 8 ###########################################################################################

def compute_score(board):
    N = len(board)
    totalScore = 0
    # Use nested for loops to add up the pieces on the board to calculate the score        
    return totalScore

def process_leaderboard(leaderboard, current_game_score):
    # First, calculate the total number of scores currently in the leaderboard


    # Then compare the current_game_score to existing scores to determine
    # if the current_game_score should be stored in the leaderboard.


    # If the current score is a high score, prompt the user for their name
    # with input()
    # # # # If there are already five scores stored in the leaderboard, you
    # # # # will need to determine which score to remove and remove it so that
    # # # # the new current score can fit (max of 5 scores in leaderboard)
    #
    # Finally, add/update the Name in the leaderboard with the current score

    # You do not need to return anything from this function, changes made to leaderboard
    # will reflect elsewhere in the code.
    pass


def print_leaderboard(leaderboard):
    ## Do not change the next two lines of code ####################
    import copy
    copied_leaderboard = copy.deepcopy(leaderboard)
    ## This will be very similar to the Part 2 of A59, where you needed to remove values
    ## from the dictionary in order to figure out the rankings of word frequencies.
    ## Since the leaderboard needs to remain unchanged for the next game, we can make a
    ## COPY of the leaderboard in the variable copied_leaderboard. Do not pop() values from
    ## the main leaderboard variable in this function, only change copied_leaderboard.
    clear()
    print("Printing of high scores not yet implemented.")
    print()

    # Your code here

#End of third section

############################################################################################################
################################## DO NOT CHANGE ANYTHING BELOW THIS LINE ##################################   - Section 4 -
############################################################################################################

try:
    from utils import *
except ImportError:
    print('Could not import utils... bye!')
    quit(-1)

import subprocess
import sys

if __name__ == "__main__":
    #Install package dependencies
    ''' MILLER - Compat error w/getch --- oh well.
    try:
        print('Please stand by... validating getch/termcolor status...\n...')
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-q', 'getch'])
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-q', 'termcolor'])
        print('Successfully installed packages! You may need to restart the game in order to enable terminal colors. Press enter to continue...')
        input()
    except:
        print('Unable to install one or more packages, terminal will not be colorized. Press enter to continue...')
        input()
    '''

    #Only want to see the game board at the top
    clear()
    
    #Starting the game
    main()
