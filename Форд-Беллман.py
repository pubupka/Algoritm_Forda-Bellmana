from math import inf
import numpy as np

def cycle(lam_before, C):
    answer = input("Проверить наличие цикла с отрицательным весом? (да/нет) ")
    if answer == "да":
        lam = []
        for j in range(n):
            array = []
            column = C[:, j]
            for k in range(n):
                array.append(lam_before[k] + column[k])
            lam.append(min(array))
        if lam == lam_before:
            print("Цикла с отрицательным весом не наблюдается")
        else:
            print("Имеется цикл с отрицательным весом")
    print("Хорошего дня и отличного настроения!")

i = inf
n = 6
C = np.array([[0, 7, 9, i, 11, i],
              [i, 0, 6, 6, i, 13],
              [i, i, 0, 5, 6, i],
              [i, i, i, 0, i, i],
              [i,  4, i, 6, 0, 8],
              [i, i, i, 7, i, 0]])

start = int(input("С какой вершины начинаем? ")) - 1

lam_before = [i, i, i, i, i, i]
lam_before[start] = 0
i = 0

for i in range(n):
    lam = []
    for j in range(n):
        array = []
        column = C[:, j]
        for k in range(n):
            array.append(lam_before[k] + column[k])
        lam.append(min(array))
    if lam == lam_before:
        break
    lam_before = lam[:]

print()
for i in range(len(lam)):
    if lam[i] == inf:
        print(f"От вершины '{start + 1}' до вершины '{i + 1}' добраться нельзя")
        continue
    print(f"Расстояние от вершины '{start + 1}' до вершины '{i + 1}' равно {lam[i]}")
print()

cycle(lam, C)
