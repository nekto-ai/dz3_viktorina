# (МОДУЛЬ 2) bornyear.py
actual_year = 1799
actual_day = 26

def get_year():
    input_year = int(input("Введите год рождения Пушкина: "))
    if(len(str(input_year)) == 4):
        return input_year
    else:
        print("Это должно бвть четырехзначное число.")
        get_year()

def get_day():
    birthday = int(input("Пушкин родился в мае. Введите какого числа: "))
    if(birthday >= 1 and birthday <= 31):
        return birthday
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



