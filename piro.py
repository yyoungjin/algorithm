# 2239
import sys
sys.setrecursionlimit(10**7)

table = []
zeros = []
for i in range(9):
    tmp = list(map(int, input()))
    table.append(tmp)
    for j in range(9):
        if not tmp[j]:
            zeros.append((i, j))

row_arr = []
for i in range(9):
    tmp = set(table[i])
    row_arr.append(tmp)

columns = list(zip(*table))
col_arr = []
for i in range(9):
    tmp = set(columns[i])
    col_arr.append(tmp)

square_arr = [[],[],[]]
for i in range(3):
    I = i * 3
    for j in range(3):
        j *= 3
        tmp = set()
        for s in range(3):
            tmp.add(table[I+s][j])
            tmp.add(table[I+s][j+1])
            tmp.add(table[I+s][j+2])
        square_arr[i].append(tmp)


def promising(x, y, num):
    if num in row_arr[x]:
        return False
    elif num in col_arr[y]:
        return False
    elif num in square_arr[x//3][y//3]:
        return False
    return True


def backtrack(depth):
    if depth == len(zeros):
        for t in table:
            print(''.join(map(str, t)))
        exit()

    i, j = zeros[depth] # 확인할 위치
    for num in range(1, 10):
        if promising(i, j, num):
            row_arr[i].add(num)
            col_arr[j].add(num)
            square_arr[i//3][j//3].add(num)
            table[i][j] = num

            backtrack(depth+1)

            table[i][j] = 0
            row_arr[i].remove(num)
            col_arr[j].remove(num)
            square_arr[i//3][j//3].remove(num)


backtrack(0)