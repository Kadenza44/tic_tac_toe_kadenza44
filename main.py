
# Проверка на победу
def chech_victory():
    victory = 0
    check_diag_1 = []  # cюда добавим значения по диагонали 1
    check_diag_2 = []  # сюда добавим значения по диагонали 2

    for x in range(len(game_field)):
        check_diag_1.append(game_field[x][-1 - x])
        check_diag_2.append(game_field[x][x])
        check_col = []  # сюда добавим значения по колонкам
        check_row = []  # сюда добавим значения по рядам
        for y in range(len(game_field)):
            check_col.append(game_field[y][x])
            check_row.append(game_field[x][y])
        if set(check_col) == {'x'} or set(check_col) == {'0'}:
            victory = 1
        elif set(check_row) == {'x'} or set(check_row) == {'0'}:
            victory = 1

    if set(check_diag_1) == {'x'} or set(check_diag_1) == {'0'}:
        victory = 1
    elif set(check_diag_2) == {'x'} or set(check_diag_2) == {'0'}:
        victory = 1  # победа

    return victory

# Отрисовка игрового поля
def show_game_field():
    row_num = []
    for i in range(97, 97+len(game_field), 1):
        row_num.append(chr(i))
    print(' ', *row_num)
    for i in range(len(game_field)):
        print(i+1, *game_field[i])

while True:
    try:
        size_game_field = int(input('Введите размер игрового поля от 3 до 9: '))
        if 3 <= size_game_field <= 9:
            break
        else:
            print('Значение не убирается в диапазон 3...9')
    except:
        print('Введите верное значение')

game_field = [['-'] * size_game_field for i in range(size_game_field)]  # генерируем игровое поле
User_1 = input('Игрок-1, представься: ')
User_2 = input('Игрок-2, представься: ')
print()
print(User_1 + ', приветствуем тебя, твой символ x')
print(User_2 + ', приветствуем тебя, твой символ 0')
show_game_field()

while chech_victory() == 0:

    while True:
        step_user_1 = input(User_1 + ', Ваш ход, (пример: 1b): ')
        try:
            x = int(list(step_user_1)[0]) - 1
            y = ord(list(step_user_1)[1]) - 97
            if game_field[x][y] == '-':
                game_field[x][y] = 'x'
                break
            else:
                print('Этот ход уже сделан')
        except:
            print('НЕКОРРЕКТНЫЙ ВВОД')
    show_game_field()
    if chech_victory() == 1:
        print(User_1, ', Поздравляем с победой!!!')
        break

    while True:
        step_user_2 = input(User_2 + ', Ваш ход, (пример: 1b): ')
        try:
            x = int(list(step_user_2)[0]) - 1
            y = ord(list(step_user_2)[1]) - 97
            if game_field[x][y] == '-':
                game_field[x][y] = '0'
                break
            else:
                print('Этот ход уже сделан')
        except:
            print('НЕКОРРЕКТНЫЙ ВВОД')
    show_game_field()
    chech_victory()
    if chech_victory() == 1:
        print(User_2, ', Поздравляем с победой!!!')
        break




