# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

from random import randint


def CreateRandomList(min, max, size):
    return [randint(min, max+1) for x in range(size)]


N = int(input("Введите N, кол-во кустов: "))
bushes = CreateRandomList(20, 50, N)
print(bushes)
res = 0
index = 0
for i in range(3, len(bushes)+3):
    if len(bushes) < 3:
        print("Не хватает кустов на грядке! ")
        break
    bushes = bushes[1:] + bushes[:1]
    tmp = bushes[0] + bushes[1] + bushes[2]
    if tmp > res:
        res = tmp
        index = i
print("Всего ягод", res, "на кустах №", index-1, index, index+1)
    




