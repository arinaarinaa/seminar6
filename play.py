#Программа для игры в крестики-нолики 

maps = [1,2,3,
        4,5,6,
        7,8,9]   #Здесь выбирает цифру игрок
victories = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]   #случаи выигрыша

def print_maps():
    print(maps[0], end =' ')
    print(maps[1], end = ' ')
    print(maps[2])

    print(maps[3], end = ' ')
    print(maps[4], end = ' ')
    print(maps[5])

    print(maps[6], end = ' ')
    print(maps[7], end = ' ')
    print(maps[8])

def step_maps(step,symbol): #Функция, туда вкладываем цифру + символ
    ind = maps.index(step) # тут встроенная функция (сама определяет индекс по цифре)
    maps[ind] = symbol #замена цифры с этим индексом на символ

def get_result():
    win = ''
    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            win = 'X'
        if maps[i[0]]== '0' and maps [i[1]] == '0' and maps[i[2]] == '0':
            win = '0'
    return win


Game_over = False
player1 = True #Константа для начала - идем по функции пока не буит неправильно 

while Game_over == False:
    print_maps()
    if player1 == True:
        symbol = 'X'
        step = int(input('Игрок 1, ваш ход - \n'))
    else:
        symbol = '0'
        step = int(input('Игрок 2, ваш ход - \n'))
    step_maps(step, symbol)
    win = get_result()
    if win!='':
        Game_over =True
    else:
        Game_over =False
    player1= not(player1)
print_maps()
print('Победил', win)


