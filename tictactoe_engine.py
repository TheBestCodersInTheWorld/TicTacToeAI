import random
import sys

# TODO
# Set the size of the tic tac toe board with two global variables
BOARD_HEIGHT = 3
BOARD_WIDTH = 3

# Dictionary mapping position numbers to board coordinates
coords = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1),9: (2, 2)}

def get_all_winning_lines() -> list:
    """
    This function will return all the combinatinos of positions on a tictactoe board
    that can make a player win, meaning all possible positions that make up a line of three
    filled boxes in a row.

    example: 
    For the below board, one such combination is [1,5,9], this makes up the diagonal 
    from top left to bottom right.

      | 2| 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9

    Returns:
        list: list of lists, where inner lists are a possible combination.
    """
    all_winning_lines = [[1,4,7], [2,5,8], [3,6,9], [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7]]
        

    # TODO
    # Create all_winning_lines using for loops.
    # Don't worry about the diagonals
    # for all_winning_lines in range(0,8):
    #     get_all_winning_lines()

    cols = []
    for width_pos in range(1, BOARD_WIDTH + 1):
        col = list(range(width_pos, BOARD_HEIGHT * BOARD_WIDTH + 1, BOARD_WIDTH))
        cols.append(col)

    rows = []
    for height_pos in range (1, BOARD_HEIGHT * BOARD_WIDTH, 3):
        row = list(range(height_pos, height_pos + BOARD_WIDTH))
        rows.append(row)


    diagonals = [list(range(1,10, 4)), list(range(3,8,2))]

    return all_winning_lines
three_in_a_row = get_all_winning_lines()


def new_board() -> list:
    """
    This function will create a new, blank, tic-tac-toe board, using
    a 2D array.
    """

    board = []
    for row in range(BOARD_HEIGHT):
        new_row = []
        for columns in range(BOARD_WIDTH):
            new_row.append(None)
        board.append(new_row)
    return board

def get_winner(board: list) -> str:

    """
    This function will look at the board and check if a player has won. 
    If a player won, it returns the winning player's symbol. Otherwise, 
    it returns None.

    Args:
        board (list): The list that is the tic-tac-toe board
    """


    for three_in_row in three_in_a_row:
        line_values = []
        for space in three_in_row:  

            row = coords[space] [0]
            column = coords[space][1]
            line_values.append(board[row][column])
            

        if set(line_values) == {"X"}:
            return "X"
        if set(line_values) == {"O"}:
            return "O"

            #  OUR BOARD
            #     None | O |  None
            #       -----------
            #     None | X |  None
            #        -----------
            #     None | X | None


            #  POSITIONS OF THE BOARD
            #     1 |  2 | 3
            #    -----------
            #      4 | 5 | 6
            #    -----------
            #     7 |  8  | 9
        return None



    # TODO
    # Check if our board contains any lines of three X's in a row or three O's in a row. 
    # If it does, then return the winning symbol
    # by taking any position from the winning line.

    # Return None if no winner is found
    return None



          # Add diagonal from top left to bottom right
            #     1 |  2 | 3
            #    -----------
            #     4 | 5 | 6
            #    -----------
            #     7 |  8  | 9

    return cols + rows + diagonals


def render(board):
    """
    This function takes in the current board, and prints it to the command line so
    we can see it. It does not return anything.

    Args:
        board (list): The current tic tac toe board
    """

    rows = []
    for y in range(0, BOARD_HEIGHT):
        row = list(board[y])
        rows.append(row)
    
    row_num = 0
    # print( '  0 1 2 ')
    print ('  ------')
    for row in rows:
        output_row = ''
        for sq in row:
            if sq is None:
                output_row += ' '
            else:
                output_row += sq
        print (" |%s |" % (' '.join(output_row)))
        row_num += 1
    print ('  ------')



def make_move(symbol, board, move_coords):
    """
    Places the symbol at the specified coordinates on the board.

    Args:
        symbol (str): the symbol we are placing, X or O
        board (list): our board
        move_coords (tuple): our move coordinates

    From get_move
        if board[position[0]][postition[1]] == None:

      x |  | o
    ---------
    None | x | None
    ---------
    None | x | o

    """
    board[move_coords[0]][move_coords[1]] = symbol

    # TODO make the move.
    

def make_move_pos(symbol, board, position_num):
    """
    Places the symbol at the specified position on the board
    
    Args:
        symbol (str): [description]
        board (list): [description]
        move_co_ords (tuple): [description]
    """
    
    valid_move = False
    while not valid_move:
        # TODO
        # Use an if statement to check if the position is valid.
        pass

def is_board_full(board):
    """
    Checks if the board is completely full and if there are no more free spaces.

    Args:
        board (list): The current board

    Returns:
        True if the board is full, False otherwise

    """

    for horizontal_row in board:
        for vertical_column in horizontal_row:
            if vertical_column == None:
                return False
    return True



def get_move(board, current_player_symbol, current_player_name):
    """
    Get the move from the player

    Args:
        board ([type]): [description]
        player_symbol ([type]): [description]

    x | None | o
    ---------
    None | x | None
    ---------
    None | x | o

    coords[5]
    Returns: the move coordinates for the chosen move    
    """    
    # "input(<message>)" will give us back whatever the player types in 

    # position = (1,3)
    # board[][]

    space_number = int(input("type the position you want to place your piece:"))
    position = coords[space_number]
    if board[position[0]][position[1]] == None:
        return position
    else:
        print("this spot is already taken")

def play(p1_name, p2_name):
    """
    This function triggers the game play.

    Args:
        p1_name ([type]): [description]
        p2_name ([type]): [description]
    """

    # Declare the two players of the game
    players = [
        ('X', p1_name),
        ('O', p2_name),
    ]


    # Start a fresh game at 0 turns so far, and a new board
    turn_number = 0
    board = new_board()
    no_winner = True

    # Continue the game until a winner is found
    while no_winner:
        # Choose the player who is taking the turn
        current_player_symbol, current_player_name = players[turn_number % 2]
        render(board)

        # Take the move position from the player and mark it on the baord
        move_position = get_move(board, current_player_symbol, current_player_name)
        make_move(current_player_symbol, board, move_position)

        # Check if there is a winner
        winner = get_winner(board)

        if winner is not None:
            no_winner = False
            render(board)
            print ("THE WINNER IS %s!" % winner)
            break

        if is_board_full(board):
            render(board)
            print ("IT'S A DRAW!")
            break

        turn_number += 1

