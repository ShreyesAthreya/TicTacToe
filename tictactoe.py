from modules import *

print("Welcome to Tic Tac Toe")
while True:
    the_board = [" "] * 10
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + ' will play first')
    play_game = input("Press 'y' if you wish to play")
    if play_game == 'y':
        game = True
    else:
        game = False
    while game:
        print("H")
        if turn == 'Player 1':
            show_board(the_board)
            print("Player 1 da")
            position = player_choise(the_board)
            place_marker(the_board, player1, position)
            if has_won(player1, the_board):

                show_board(the_board)
                print("Player 1 has won")
                game = False
            else:
                if full_board(the_board):
                    show_board(the_board)
                    print("The game is a tie")
                    game = False
                else:
                    turn = "Player 2"
        else:
            if turn == 'Player 2':
                show_board(the_board)
                print("Player 2 da")
                position = player_choise(the_board)
                place_marker(the_board, player2, position)
                if has_won(player2, the_board):

                    show_board(the_board)
                    print("Player 2 has won")
                    game = False
                else:
                    if full_board(the_board):
                        show_board(the_board)
                        print("The game is a tie")
                        game = False
                    else:
                        turn = "Player 1"
    if not replay():
        break
