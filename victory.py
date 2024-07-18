# (МОДУЛЬ 6) victory.py

greeting = 'Играем! Викторина на знание года рождения знаменитости!'
count_right_answer = 0
total_questions = 0

celebrities = [('поэт Пушкин', 1799), 
               ('маршал Жуков', 1896),
               ('певец Шаман', 1991),
               ('актер Данила Козловский', 1985),
               ('актриса Милла Йовович', 1975)]

total_questions = len(celebrities)

def reset_counter():
    count_right_answer = 0

def get_year(celebrity):
    input_year_str = input(f'Введите в каком году родил(ся)/(ась) {celebrity[0]} ')
    if(input_year_str.isnumeric() and len(input_year_str) == 4):
        return int(input_year_str)
    else:
        print('Неправильный ответ! Вводите четырехзначное число.')
        return -1

print(greeting)

play_again = True
while play_again:
    for celebrity in celebrities:
        if(get_year(celebrity) == celebrity[1]):
            count_right_answer += 1
            print('Отлично!')
        else:
            print('Неправильный ответ!')

    score = (count_right_answer*100)/total_questions
    print(f'Ваш результат: {score}')
    print(f'Всего правильных ответов: {count_right_answer} из 5')
    print('Если хотите сыграть еще введите 1, если нет, то 0 ')
    repeat_str = input('Итак, введите ваш ответ: ')
    if(repeat_str.isnumeric() and repeat_str == '0'):
        play_again = False
    else:
        print(greeting)
        reset_counter()
        
print('Игрв закончена!')






