import math
def square (length):
    return math.ceil(length*length)
num = int(input("Введите сторону квадрата: "))
result = square (num)
print ("Площадь квадрата со стороной ", num, " = ", result)