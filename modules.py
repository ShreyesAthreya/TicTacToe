import random


def show_board(board):
    """
    Print board and 10 new lines
    """
    print("\n" * 10)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def player_input():
    """
    :rtype: Tuple
    Output will return a tuple
    :return: Tuple X,O or O,X
    """
    marker = 'Hold dummy value'
    while marker != "X" and marker != "O":
        marker = input("Player1: Choose your marker 'X' or 'O'").upper()
    if marker == 'X':
        return 'X', 'O'
    return "O", "X"


def place_marker(board, marker, position):
    """
    Replace boad char in position with marker
    """
    board[position] = marker


def has_won(marker, board):
    """
    Checks all rows, columns and the two diagonals
    :param marker: player1 or player2
    :param board: the board
    :rtype: Bool
    """
    return (board[1] == board[2] and board[2] == board[3] and board[3] == marker) or (
            board[4] == board[5] and board[5] == board[6] and board[6] == marker) or (
                   board[7] == board[8] and board[8] == board[9] and board[9] == marker) or (
                   board[1] == board[4] and board[4] == board[7] and board[7] == marker) or (
                   board[2] == board[5] and board[5] == board[8] and board[8] == marker) or (
                   board[3] == board[6] and board[6] == board[9] and board[9] == marker) or (
                   board[1] == board[5] and board[5] == board[9] and board[9] == marker) or (
                   board[3] == board[5] and board[5] == board[7] and board[7] == marker)


def choose_first():
    rand = random.randint(1, 2)
    if rand == 1:
        return "Player 1"
    return "Player 2"


def available(board, position):
    return board[position] == ' '


def full_board(board):
    """
    We use available() to check if there is any empty spaces,
    once there are no empty spaces, it concludes the board is full
    :return: Board is full if return is True
    """
    for i in range(1, 10):
        if available(board, i):
            return False
    return True


def player_choise(board):
    position = 0
    while position not in range(1, 10) or not available(board, position):
        position = int(input("Choose position: (1-9)"))
    return position


def replay():
    ans = input("Enter 'Yes' if you wish to replay").upper()
    return ans == "YES"
