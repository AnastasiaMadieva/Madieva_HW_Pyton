def is_year_leap (YYYY):
    return "True" if YYYY % 4 == 0 else "False"
num = int(input("Введите год: "))
result = is_year_leap (num)
print ("Является ли ", num, "год високосным? ", result)