from random import shuffle

a = list(range(0, 16))
shuffle(a)
field = [a[:4], a[4:8], a[8:12], a[12:]]
# field = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]

for i in range(4):
    for j in range(4):
        if field[i][j] == 0:
            zero = (i, j)


def print_field(f):
    for i in f:
        for j in i:
            if j < 10:
                print(j, ' ', end='')
            else:
                print(j, end=' ')
        print('\n', end='')


print_field(field)
count = 1
while True:
    print('Ход', count)
    print('Введите координаты сдвигаемой костяшки через пробел: ')
    s = [int(_) for _ in input().split()]
    if len(s) == 2:
        x, y = s[0] - 1, s[1] - 1
        if x < 0 or x > 15 or y < 0 or y > 15:
            continue
    else:
        continue
    xy = (x, y)
    z, w = zero[0], zero[1]
    if not((x == z and abs(y - w) == 1) or (y == w and abs(x - z) == 1)):
        continue
    zero = xy
    xy = (z, w)
    
    field[xy[0]][xy[1]] = field[zero[0]][zero[1]]
    field[zero[0]][zero[1]] = 0
    print_field(field)
    count += 1
    
    if field == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        print(f'Поздравляю! Вы выиграли за {count} ходов!')
        break
