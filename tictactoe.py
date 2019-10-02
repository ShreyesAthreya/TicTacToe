from modules import *

print("Welcome to Tic Tac Toe")
while True:
    the_board = [" "] * 10
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + 'will play first')
