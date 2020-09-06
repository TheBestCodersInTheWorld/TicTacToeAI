import copy
import tictactoe_engine as tt

def minimax_move(board, symbol):
    """
    This function figures out what is the best move to take in "board", for the 
    player using "symbol" ("X" or "O")

    Args:
        board: The current tic tac toe board
        symbol: The game symbol of the AI
    
    Returns: The best position to move on the board

    """
     # These variables will hold the best move and score the AI can take
    best_move = None
    best_score = None

    # write some code here
    # get all the legal moves, which are the blank spaces
    for move in all_legal_moves(board):
        # Make a copy of the board
        copied_board = copy.deepcopy(board)
        tt.make_move(symbol, board, move)
        
        # - CALL THE RECURSIVE FUNCTION TO SCORE THE BOARD
        opponent = get_opponent(symbol)
        new_score = bestScore(copied_board, opponent, symbol)

        if best_score == None or best_score < new_score:
            best_score = new_score
            best_move = move

    return best_move

def bestScore(board, player_to_move, player_to_optimize):
    """
    Returns: The best score for the current board for the player_to_optimize
    """
    # Base Cases:
    possible_winner = tt.get_winner(board)
    if possible_winner != None:
        if possible_winner == player_to_optimize:
            return 1
        else:
            return -1
    if tt.is_board_full(board):
        return 0

    # Recursive Case
    # -- 
    lots_of_scores = []
    for space in all_legal_moves(board):
        new_board = copy.deepcopy(board)
        tt.make_move(player_to_move, new_board, space)
        player = get_opponent(player_to_move)
        best_score = bestScore(new_board, player, player_to_optimize)
        lots_of_scores.append(best_score)
        
    if player_to_move == player_to_optimize:
        return max(lots_of_scores)
    else:
        return min(lots_of_scores)
    
    

def get_opponent(player):
    """
    This function determines who the opponent of "player" is
    Args:
        player: "X" or "O"
    Returns: 
        the opponent of player, "X" or "O"
    """
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    return opponent
    

# def make_move(symbol, board, move_coords):

#     board[move_coords[0]][move_coords[1]] = symbol


def all_legal_moves(board):
    """
    This function figures out what spaces are taken and what moves are legal

    Args: 
    board: the current tic tac toe board

    Returns: 
    a list of all the legal moves (coordinates)
    """
    legal_moves = []
    
    for row in range(len(board)):
        for column in range(len(board)):
            #if board at this row, and this column is empty
            if board[row][column] == None:
                legal_moves.append((row, column))
    return legal_moves
                

    

