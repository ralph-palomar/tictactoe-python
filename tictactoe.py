# Validates the marker if either X or O.
def validate_marker(marker):
    return marker == 'X' or marker == 'O'


# Assigns markers to Player 1 and 2 one way or the other.
def assign_player2_marker(marker):
    if marker == 'X':
        return 'O'
    else:
        return 'X'


# Validates the number is only from 1 to 9.
def a_valid_pick(num):
    return num in range(1, 10)


# Determines if the given number is even or odd.
def an_even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


# Validates the current board.
def an_occupied_cell(pick_num, current_board):
    cell = current_board[int(pick_num) - 1]
    return cell == 'X' or cell == 'O'


# Updates the current board.
def update_board(pick_num, player_mark, current_board):
    current_board[int(pick_num) - 1] = player_mark
    return current_board


# Displays the current board.
def display_board(current_board):
    print()
    print(" {} | {} | {} ".format(current_board[0], current_board[1], current_board[2]))
    print("-----------")
    print(" {} | {} | {} ".format(current_board[3], current_board[4], current_board[5]))
    print("-----------")
    print(" {} | {} | {} ".format(current_board[6], current_board[7], current_board[8]))


# Checks if the board is full.
def full_board(current_board):
    return not (' ' in current_board)


# Checks if there is already a winner.
def check_winner(current_board):
    winning_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combo:
        player_x = 0
        player_o = 0
        for pos in combo:
            if current_board[pos] == 'X':
                player_x += 1
            elif current_board[pos] == 'O':
                player_o += 1
            else:
                pass
        if player_x == 3:
            result = 'X'
            break
        elif player_o == 3:
            result = 'O'
            break
        else:
            result = '#'
    return result


# Initialize variables.
game_on = True
turn = 1
markers = ['#']
board = [' '] * 9

print("\nWelcome to Tic Tac Toe!")
display_board(board)
player1 = input("\nPlease pick a marker 'X' or 'O': ")

while not validate_marker(player1):
    player1 = input("\nInvalid! Please pick a marker 'X' or 'O': ")
else:
    player2 = assign_player2_marker(player1)
    markers.append(player1)
    markers.append(player2)

while game_on:
    order = an_even_odd(turn)
    if order == "ODD":
        whose_turn = "1"
    else:
        whose_turn = "2"

    if full_board(board):
        print("\nBoard is full! Game over!")
        break

    pick = int(input("\nPlayer {} >> Enter a cell number from 1-9 that is not occupied: ".format(whose_turn)))
    while (not a_valid_pick(pick)) or an_occupied_cell(pick, board):
        if not a_valid_pick(pick):
            display_board(board)
            pick = int(input("\nInvalid! Player {} >> Enter a cell number from 1-9: ".format(whose_turn)))
        elif an_occupied_cell(pick, board):
            display_board(board)
            pick = int(input("\nOccupied! Player {} >> Enter a different cell number: ".format(whose_turn)))
        else:
            pass
    else:
        turn += 1
        board = update_board(pick, markers[int(whose_turn)], board)
        display_board(board)
        winner = check_winner(board)
        player_num = markers.index(winner)
        if player_num == 1:
            print("\nPlayer 1 Wins! Game over!")
            break
        elif player_num == 2:
            print("\nPlayer 2 Wins! Game over!")
            break
        else:
            pass

