from tictactoe_engine import play
import sys


from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

if __name__ == "__main__":

    cprint(figlet_format('TicTacToe', font='doh'),
       'red', attrs=['bold'])

    while 1:
        try:
            player_1 = str(input("Enter Player 1's name:"))
            player_2 = str(input("Enter Player 2's name:"))
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("invalid name input, enter player names again")
    play(player_1, player_2)
    