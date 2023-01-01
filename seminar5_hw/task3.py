# Создайте программу для игры в "Крестики-нолики".

print()
print("Крестики-нолики")
print()

board = list(range(1, 10))


def board_design(board):
    for i in range(3):
        print(' ', board[0+i*3], ' ', board[1+i*3], ' ', board[2+i*3])
        print()


def moves(player):
    valid = False
    while not valid:
        player_move = int(input("Ваш ход: "))
        if 1 <= player_move <= 9:
            if (str(board[player_move - 1]) not in "XO"):
                board[player_move-1] = player
                valid = True
        else:
            print("Попробуйте еще раз")


def win_check(board):
    win_squares = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for i in win_squares:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def gameplay(board):
    count = 0
    win = False
    while not win:
        board_design(board)
        if count % 2 == 0:
            moves("X")
        else:
            moves("O")
        count += 1
        if count > 4:
            temp = win_check(board)
            if temp:
                print(temp, "победил")
                win = True
                break
        if count == 9:
            print("Ничья!")
            break
    print()
    board_design(board)


gameplay(board)