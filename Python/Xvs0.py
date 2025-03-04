field = [str(i) for i in range(1, 10)]
print(field)

def render(field):
    print('-------')
    for i in range(0, 9, 3):
        print('|' + field[i] + '|' + field[i + 1] + '|' + field[i + 2] + '|')
    print('-------')

def check_win(field):
    win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in win_comb:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return True

def start_game(field):
    token = 'O'
    step = 0
    while True:
        render(field)
        print(f'Ход {token}:')
        user_choose = int(input('Введите номер клетки для хода'))
        if field[user_choose - 1] != 'X' and field[user_choose - 1] != 'O':
            field[user_choose - 1] = token
            if token == 'X':
                token = 'O'
            else:
                token = 'X'
            step += 1
        else:
            print('клетка занята')
        if check_win(field):
            if token == 'O':
                print(f'WIN X')
            else:
                 print(f'WIN O')
            break
        if step == 9:
            print('НИЧЬЯ')
            break

start_game(field)
