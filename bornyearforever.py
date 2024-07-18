# (МОДУЛЬ 4) bornyearforever.py
actual_year = 1799

def get_year():
    input_year_str = input('Введите год рождения Пушкина: ')
    if(input_year_str.isnumeric() and len(input_year_str) == 4):
        return int(input_year_str)
    else:
        print("Это должно быть четырехзначное число.")
        return -1

while(get_year() != actual_year):
    print('Неверно')

print('Верно')

