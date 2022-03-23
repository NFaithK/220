"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    ret = []
    for i in range(1, 10):
        ret.append(i)
    return ret


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    legal = str(board[position - 1]).isnumeric()
    return legal


def fill_spot(board, position, character):
    str(board[position - 1]).replace(position, character)



def winning_game(board):
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[3] == board[6] == board[9]:
        return True
    if board[1] == board[2] == board[3]:
        return True
    if board[4] == board[5] == board[6]:
        return True
    if board[7] == board[8] == board[9]:
        return True
    if board[1] == board[5] == board[9]:
        return True
    if board[3] == board[5] == board[7]:
        return True
    else:
        return False



def game_over(board):
    for position in range(1,10):
        if is_legal(board,position):
            return False
        if winning_game(board):
            return True


def get_winner(board):
    acc_o= 0
    acc_x = 0

    if game_over(board) is False:
        return False
    counters = " "
    for position in (0,9)
        board_count = board_count + counters

    if character[x] > character[o]:
        return print("congrats! x wins!")


def play(board):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
