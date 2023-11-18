from random import randint
def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board, player):
    winning_combinations=[(0, 1, 2), (3, 4, 5), (6,7,8),
                          (0,3,6), (1,4,7), (2,5,8),
                          (0,4,8),(2,4,6)]
    for combination in winning_combinations:
        if board[combination[0]]==board[combination[1]]==board[combination[2]]==player:
            return True
    return False
def get_player_move(board, player):
    get=int(input("Введите номер клетки: "))
    if get>=1 and get<=9 and board[get-1]==" ":
        board[get-1]=player
        return board
    else:
        print("Ошибка")
        return get_player_move(board, player)
def get_computer_move(board, player):
    get=randint(1,9)
    if get>=1 and get<=9 and board[get-1]==" ":
        board[get-1]=player
        return board
    else:
        return get_computer_move(board, player)    
def main():
    map1=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("карта:")
    draw_board(map1)
    print("Первым хожит X, за кого ты будешь играть?")
    print("1: X")
    print("2: 0")
    f=1
    while f!=0:
        b=int(input())
        if b==1 or b==2:
            f=0
        else: print("Ошибка")
    if b==1:
        a=["X","0"]
    else:
        a=["0","X"]
    ch=1
    
    draw_board(board)
    while " " in board != True:
        if b==2:
            print("Ход компьютера:")
            get_computer_move(board, a[1])
            draw_board(board)
            b-=1
        
        print("Ход игрока:")
        get_player_move(board, a[0])
        draw_board(board)
        if check_win(board, a[0])==True:
            print("Игрок победил!")
            ch=0
            break
        if " " in board ==False:
            break
        
        print("Ход компьютера:")
        get_computer_move(board, a[1])
        draw_board(board)
        if check_win(board, a[1])==True:
            print("Компьютер победил!")
            ch=0
            break
    if " " in board ==False and ch==1:
        print("Ничья")


main()