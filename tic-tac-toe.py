turn = "X"
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
     
def print_board(): #  Создание игровой зоны
   
    print("---------")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("---------")  

def get_pos():
    pos =  input("Enter the coordinates: ").split()
    return pos
     
def change_turn():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
def is_winner(): #  Определение выигрышных комбинаций
    winner = False
    winner_combo = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
                      [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                       [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    for combo in winner_combo:
        line = []
        for x in combo:
            if board[x[0]][x[1]] == turn:
                line.append(True)
            else:
                line.append(False)
        if all(line):
            winner = True
            return winner
            
def player_move(): #  Определение всех условий для хода и ввода данных
    coordinates = get_pos() 
    if not (coordinates[0].isdigit() and coordinates[1].isdigit()):
        print("You should enter numbers!")
        player_move()
    elif int(coordinates[0]) not in range(1, 4) or int(coordinates[1]) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        player_move()
    else:
        x, y = (int(coordinates[0]) - 1), (int(coordinates[1]) - 1)
        if board[x][y] == " ":
            board[x][y] = turn
            print_board()
            if is_winner(): #  Определение победителя
                print(turn, "wins")
                return 
            else:
                
                if any(" " in sl for sl in board):                    
                    change_turn()
                    player_move()
                else:
                    print("Draw")
                    return 
        else:
            print("This cell is occupied! Choose another one!")
            player_move()
# Запуск игры           
print_board() 
player_move()
