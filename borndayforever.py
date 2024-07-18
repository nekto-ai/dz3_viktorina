# (МОДУЛЬ 5) borndayforever.py
actual_year = 1799
actual_day = 26

def get_year():
    input_year_str = input("Введите год рождения Пушкина: ")
    if(len(input_year_str) == 4 and input_year_str.isnumeric()):
        return int(input_year_str)
    else:
        print("Это должно бвть четырехзначное число.")
        return -1

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
        print('Число должно быть от 1 до 31.')
        return -1

   

while(get_year() != actual_year):
    print('Неверный год рождения')

print('Верно')

while(get_day() != actual_day):
    print('Неверный день рождения')

print('Верно')