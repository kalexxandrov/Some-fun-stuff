import random
import datetime


def pick(): # выбор цивилизации
    global daniil_civ
    global kirill_civ
    
    while True:
        daniil_civ = random.choice(civilizations1) 
        del civilizations1[civilizations1.index(daniil_civ)] # исключаем последующее дублирование
        kirill_civ = random.choice(civilizations2)
        del civilizations2[civilizations2.index(kirill_civ)]

        if daniil_civ[0] != kirill_civ[0]: # исключаем возможные дропы одинаковых лидеров
            print()
            print('----------------')
            print(f'Даниил: {daniil_civ}') 
            print(f'Кирилл: {kirill_civ}')
            print('----------------')
            print()
            break
        else:
            continue


def reroll(): # реролл цивилизации (за сессию каждый может реролльнуть цивилизацию до двух раз, если рероллит больше, то луз)
    global daniil_reroll_count
    global kirill_reroll_count
    
    while True:
        print()
        print('Кто рероллит? "К" - Кирилл, "Д" - Даниил')
        name = input('Введи "К" или "Д": ')

        if name.lower() == 'д':
            if daniil_reroll_count != 0:
                daniil_reroll_count -= 1
                print()
                print(f'Счётчик оставшихся рероллов Даниила: {daniil_reroll_count}')
                break
            else:
                print()
                print(f'У Даниила больше нет рероллов. Он отсосал! Поражение записано!')
                daniil_civs_score.update({daniil_civ: 0})
                kirill_civs_score.update({kirill_civ: 1})
            break
        elif name.lower() == 'к':
            if kirill_reroll_count != 0:
                kirill_reroll_count -= 1
                print()
                print(f'Счётчик оставшихся рероллов Кирилла: {kirill_reroll_count}')
                break
            else:
                print()
                print(f'У Кирилла больше нет рероллов. Он отсосал! Поражение записано!')
                kirill_civs_score.update({kirill_civ: 0})
                daniil_civs_score.update({daniil_civ: 1})
            break
        else:
            print('Введено что-то не то. Попробуй снова!')
            continue


def stats(): # запись результата партии
    while True:
        print()
        print('Кто выиграл? "К" - Кирилл, "Д" - Даниил')
        name = input('Введи "К" или "Д": ')
        if name.lower() == 'д':
            daniil_civs_score.update({daniil_civ: 1})
            kirill_civs_score.update({kirill_civ: 0})
            break
        elif name.lower() == 'к':
            daniil_civs_score.update({daniil_civ: 0})
            kirill_civs_score.update({kirill_civ: 1})
            break
        else:
            print('Введено что-то не то. Попробуй снова!')
            continue


def game_continue(): # проверка, не хочет ли кто ливнуть в тильте
    global flag

    while True:
        print()
        print('Продолжаем? 1 - да, 0 - нет')
        n = input('Введи число: ')
        if n == '1':
            break
        elif n == '0':
            flag = False
            break
        else:
            print()
            print('Введено что-то не то, попробуй снова!')
            continue


def game_end(): # вывод результатов и их запись в файл
    print()
    print('----------------')
    print('Результаты!')
    print()
    print(f'Общее количество побед Даниила: {list(daniil_civs_score.values()).count(1)}')
    print('Статистика Даниила: ', daniil_civs_score)
    print()
    print(f'Общее количество побед Кирилла: {list(kirill_civs_score.values()).count(1)}')
    print('Статистика Кирилла: ', kirill_civs_score)
    print()

    with open('C:/Users/Alekkir/Desktop/Civ_stats/civ_stats.txt', 'a', encoding='utf-8') as file: # запись результатов в файл
        file.write(f'Дата: {datetime.datetime.now()}\n')
        file.write(f'Общее количество побед Даниила: {list(daniil_civs_score.values()).count(1)}\n')
        file.write(f'Статистика Даниила: {daniil_civs_score}\n')
        file.write(f'Общее количество побед Кирилла: {list(kirill_civs_score.values()).count(1)}\n')
        file.write(f'Статистика Кирилла: {kirill_civs_score}\n')
        file.write('\n')

    print('Статистика записана!')
    print('----------------')


def start():
    while True:
        if flag:
            if civilizations1:
                pick()
                print('1 - реролл, 2 - записать результаты, 0 - выйти')
                n = input('Введи число: ')
                if n == '1':
                    reroll()
                    game_continue()
                elif n == '2':
                    stats()
                    game_continue()
                elif n == '0':
                    print()
                    print('Хорошо поиграли!')
                    break
                else:
                    print()
                    print('Введено что-то не то, попробуй снова!')
                    continue
            else:
                print()
                print('Цивилизации закончились! Видимо, вы удачно поиграли))')
                break
        else:
            game_end()
            break



civilizations1 = ['Авраам Линкольн', 'Александр Македонский', 'Аманиторе', 'Амбиорикс', 'Василий II', 'Виктория (Эпоха империи)', 
                    'Виктория (Эпоха паровых машин)', 'Вильгельмина', 'Ганди', 'Горго', 'Джайаварман VII',
                    'Джон Кэртин', 'Дидона', 'Елизавета I', 'Жуан III', 'Иш-Вак-Чан-Ахав', 'Кир', 'Лаутаро', 
                    'Людвиг II', 'Манса Муса', 'Матьяш I', 'Менелик II', 'Монтесума', 'Нзинга Мбанди',
                    'Надир-Шах', 'Паундмейкер', 'Пачакутек', 'Педру II', 'Перикл', 'Пётр Великий', 'Рамзес II',
                    'Саладин (визирь)', 'Саладин (султан)', 'Седжон', 'Симон Боливар', 'Сондок', 'Сулейман (Великолепный)',
                    'Сулейман (Кануни)', 'Сундиата Кейта', 'Теодор Рузвельт (Мужественный)', 'Теодор Рузвельт (Прогрессист)',
                    'Токугава', 'Траян', 'Трибхувана', 'У Цзэнтянь', 'Уилфрид Лорье', 'Феодора', 'Филипп II', 'Фридрих Барбаросса',
                    'Харальд Суровый (Варяг)', 'Харальд Суровый (Конунг)', 'Ходзё Токимунэ', 'Хубилай (Китай)', 'Хубилай (Монголия)',
                    'Цинь (Небесный мандат)', 'Цинь (Освободитель)', 'Чака', 'Чандрагупта', 'Чингисхан', 'Чьеу Тхи Чинь', 'Юлий Цезарь',
                    'Юнлэ', 'Ядвига']
civilizations2 = civilizations1.copy()

flag = True
daniil_reroll_count = 2
kirill_reroll_count = 2
daniil_civ = None
kirill_civ = None
daniil_civs_score = {}
kirill_civs_score = {}

start()
