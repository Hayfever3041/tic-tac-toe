# tic-tac-toe.py

def start():
    print('''
Welcome to tic-tac-toe.
You will be playing against a human opponent.
The coordinate should be entered as letter and then number:
    Ex. a1, b3, c2
Good luck.
''')

def player_input_func(cb):
    while True:
        player_input = input('Where would you like to go?: ')

        if player_input.startswith('a'):
            if player_input.endswith('1') and not cb[0] == ' ':
                print('That place is already taken.')
                continue
            elif player_input.endswith('2') and not cb[3] == ' ':
                print('That place is already taken.')
                continue
            elif player_input.endswith('3') and not cb[6] == ' ':
                print('That place is already taken.')
                continue
            else:
                break
        elif player_input.startswith('b'):
            if player_input.endswith('1') and not cb[1] == ' ':
                print('That place is already taken.')
                continue
            elif player_input.endswith('2') and not cb[4 == ' ']:
                print('That place is already taken.')
                continue
            elif player_input.endswith('3') and not cb[7] == ' ':
                print('That place is already taken.')
                continue
            else:
                break
        elif player_input.startswith('c'):
            if player_input.endswith('1') and not cb[2] == ' ':
                print('That place is already taken.')
                continue
            elif player_input.endswith('2') and not cb[5] == ' ':
                print('That place is already taken.')
                continue
            elif player_input.endswith('3')and not cb[8] == ' ':
                print('That place is already taken.')
                continue
            else:
                break
        else:
            print('ERROR')
            continue

    return player_input


def check(player_input, cb):
    global turn_x
    if turn_x == True:
        if player_input.startswith('a'):
            if player_input.endswith('1'):
                cb[0] = 'X'
            elif player_input.endswith('2'):
                cb[3] = 'X'
            elif player_input.endswith('3'):
               cb[6] = 'X'
        elif player_input.startswith('b'):
            if player_input.endswith('1'):
                cb[1] = 'X'
            elif player_input.endswith('2'):
                cb[4] = 'X'
            elif player_input.endswith('3'):
                cb[7] = 'X'
        elif player_input.startswith('c'):
            if player_input.endswith('1'):
                cb[2] = 'X'
            elif player_input.endswith('2'):
                cb[5] = 'X'
            elif player_input.endswith('3'):
                cb[8] = 'X'
        turn_x = False
    elif turn_x == False:
        if player_input.startswith('a'):
            if player_input.endswith('1'):
                cb[0] = 'O'
            elif player_input.endswith('2'):
                cb[3] = 'O'
            elif player_input.endswith('3'):
               cb[6] = 'O'
        elif player_input.startswith('b'):
            if player_input.endswith('1'):
                cb[1] = 'O'
            elif player_input.endswith('2'):
                cb[4] = 'O'
            elif player_input.endswith('3'):
                cb[7] = 'O'
        elif player_input.startswith('c'):
            if player_input.endswith('1'):
                cb[2] = 'O'
            elif player_input.endswith('2'):
                cb[5] = 'O'
            elif player_input.endswith('3'):
                cb[8] = 'O'
        turn_x = True

    return cb

def board(cb):
    print('''
     a   b   c
       |   |
 1   {} | {} | {}
       |   |
    -----------
       |   |
 2   {} | {} | {}
       |   |
    ------------
       |   |
 3   {} | {} | {}
       |   |
         '''.format(cb[0], cb[1], cb[2], cb[3], cb[4], cb[5], cb[6], cb[7], cb[8]))

def win_func(cb):
    if cb[0] == cb[1] == cb[2] and not cb[0] == ' ':
        print('a1 b1 c1')
        if cb[0] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[3] == cb[4] == cb[5] and not cb[3] == ' ':
        print('a2 b2 c2')
        if cb[3] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[6] == cb[7] == cb[8] and not cb[6] == ' ':
        print('a3 b3 c3')
        if cb[6] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[0] == cb[3] == cb[6] and not cb[0] == ' ':
        print('a1 a2 a3')
        if cb[0] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[1] == cb[4] == cb[7] and not cb[1] == ' ':
        print('b1 b2 b3')
        if cb[1] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[2] == cb[5] == cb[8] and not cb[2] == ' ':
        print('c1 c2 c3')
        if cb[2] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[0] == cb[4] == cb[8] and not cb[0] == ' ':
        print('a1 b2 c3')
        if cb[0] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    elif cb[2] == cb[4] == cb[6] and not cb[2] == ' ':
        print('a3 b2 c1')
        if cb[2] == 'X':
            return 'xWin'
        else:
            return 'oWin'
    else:
        pass
        return 'noWin'

def tie_func(cb):
    if not cb[0] == ' ' and not cb[1] == ' ' and not cb[2] == ' ' and not cb[3] == ' ' and not cb[4] == ' ' \
        and not cb[5] == ' ' and not cb[6] == ' ' and not cb[7] == ' ' and not cb[8] == ' ':

        return True
    else:
        return False

def play_again_func():
    play_again = input('Would you like to play again?(y/n): ')
    if play_again.startswith('y') or play_again == '':
        return True
    else:
        return False

# game
while True:
    start()

    current_board = [' ', ' ', ' ',
                    ' ', ' ', ' ',
                    ' ', ' ', ' ']
    turn_x = True
    board(current_board)

    while True:
        player_input = player_input_func(current_board)

        current_board = check(player_input, current_board)

        board(current_board)
        win = win_func(current_board)
        
        if win == 'xWin':
            print('X\'s won!')
            break
        elif win == 'oWin':
            print('O\'s won!')
            break

        if tie_func(current_board):
            print('It\'s a tie!')
            break
    if play_again_func():
        continue
    else: 
        break

