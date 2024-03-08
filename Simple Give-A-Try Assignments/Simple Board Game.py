import random
player_names = "0123456789"
try:
    rows = int(input("No. of Rows       : "))
    columns = int(input("No. of Columns    : "))
    max_points = int(input("Maximum Points    : "))
    no_of_players = int(input("Number of Players : "))
    if no_of_players > len(player_names):
        raise Exception(f'Maximum Number of Players should not exceed {len(player_names)}')
except ValueError:
    raise ValueError('You have entered Invalid Number for base 10')
except:
    raise

board = []
for i in range(rows):
    i_th_row = []
    for j in range(columns):
        i_th_row.append("*")
    board.append(i_th_row)

player_points = {}
for i in range(no_of_players):
    player_points[player_names[i]] = 0


def printing_board(li):
    for row_list in li:
        for columnar_element in row_list:
            print(columnar_element, end=" ")
        print("")
    print("\n\n\n")


printing_board(board)


while True:
    for player in player_points:

        # PLAYER Turn
        print(f"Player {player} Turn")

        die_rolling = input("Please Enter to Roll The Die : ")
        row_a = random.randint(1, rows)
        print(row_a)

        die_rolling2 = input("Please Enter to Roll The Die : ")
        col_a = random.randint(1, columns)
        print(col_a)
        print(board[(row_a - 1)][col_a - 1] not in [player, "*"])
        if board[(row_a - 1)][col_a - 1] not in [player, "*"]:
            player_points[player] += 1
        print(player_points)

        board[(row_a - 1)][col_a - 1] = player
        print(f"Point : {player_points[player]}\n\n\n")
        printing_board(board)

        if player_points[player] >= max_points:
            print(f"{player} won the game ! ")
            print(f"Points : {player_points[player]}")
            exit("Game Over")
