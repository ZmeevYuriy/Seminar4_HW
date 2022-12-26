# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import os
from random import randint

def CreateRandomList(min, max, size):
    return [randint(min, max+1) for x in range(size)]


N = int(input("Введите n - кол-во элементов первого набора: "))
M = int(input("Введите m - кол-во элементов второго набора: "))
arr1: list[int] = CreateRandomList(0, 50, N)
arr2: list[int] = CreateRandomList(0, 50, M)
print(sorted(arr1))
print(sorted(arr2))
res = []
for item in set(arr2):
    if item in set(arr1):
        res.append(item)
if len(res) == 0:
    res.append("Ничего нет!")
print("Одинаковые номера -> ", sorted(res))
    





