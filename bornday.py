# (МОДУЛЬ 2) bornyear.py
actual_year = 1799
actual_day = 26

def get_year():
    input_year_str = input("Введите год рождения Пушкина: ")
    if(len(input_year_str) == 4 and input_year_str.isnumeric()):
        return int(input_year_str)
    else:
        print("Это должно бвть четырехзначное число.")
        get_year()

def get_day():
    birthday_str = input("Пушкин родился в мае. Введите какого числа: ")
    birthday = 0
    if(birthday_str.isnumeric()):
        birthday = int(birthday_str)
    else:
        print('Введите число.')

    if(birthday >= 1 and birthday <= 31):
        return int(birthday_str)
    else:
        print('Число быть может от 1 до 31.')
        get_day()

    
if(get_year() == actual_year):
    print('Отлично!')
    if(get_day() == actual_day):
        print('Верно')
    else:
        print('Неверный день рождления')
else:
    print('Неверный год рождения')



