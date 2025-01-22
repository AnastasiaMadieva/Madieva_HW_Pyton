mm = int(input("Введите номер месяца (1-12): "))
def month_to_season(mm):
    if 1 <= mm <= 2:
        return "Зима"
    elif mm == 12:
        return "Зима"
    elif 3 <= mm <= 5:
        return "Весна"
    elif 6 <= mm <= 8:
        return "Лето"  
    elif 9 <= mm <= 11:
        return "Осень" 
    else:
        return "Неверный номер месяца"

print(month_to_season(mm)) 
