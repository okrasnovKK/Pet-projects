# '''Магический шар'''
import random
def magic_ball():
    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
               "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
               "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
               "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как Вас зовут? ')
    print('Привет, ' + name + '!')
    answer = None
    while answer != 'нет':
        input('Введите вопрос: ')
        print(random.choice(answers))
        answer = input('Продолжим? (да/нет): ')
magic_ball()




