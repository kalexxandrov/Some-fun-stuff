import random

word_list = ["отчуждение", "производство", "рационализация", "гегемония", "диктатура", "пролетариат", "абстракция",
             "диалектика", "материя", "материализм", "идеализм", "рабочий", "эксплуатация", "надстройка", "базис",
             "феодализм", "коммунизм", "социализм", "предатель", "уклонист", "сознание", "стоимость",
             "ревизионист", "воспроизводство", "революция", "промышленность", "обнищание", "кризис", "экономика",
             "капитализм", "буржуазия", "буржуй", "пролетарий", "интернационализм", "рабовладение", "неравенство",
             "равенство", "противоречие", "противоположность", "синтез", "борьба", "единство", "количество", "качество",
             "государство", "структура", "объективность", "субъективность", "отношение", "ситуация", "организованность",
             "раздробленность", "гегельянство", "радикальность", "насилие", "реформизм", "переворот", "демократия",
             "централизация", "централизм", "формация", "монополия", "олигополия", "империализм",
             "движение", "развитие", "колониализм", "закон", "меньшевизм", "большевизм", "манифест", "советы",
             "реакционизм", "реакционист", "расстрел", "гласность", "продразвёрстка", "электрификация", "демонстрация",
             "автоматизация", "забастовка", "коллективизация"]
guessed_words_count = 0


# функция выбора одного случайного слова из списка
def get_word():
    word = random.choice(word_list)
    length = len(word_list)
    for i in range(len(word_list) - 1):  # исключаем повторения
        if word_list[i] == word:
            del word_list[i]
    if len(word_list) == length:
        del word_list[-1]  # если слово было последним в списке и не проверилось циклом for
    return word


# функция отрисовки человечка
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


# функция, отвечающая за сам процесс игры
def game(word, complexity):
    # инициализируем переменные
    tries = 6
    guessed_letters = []
    guessed_words = []
    used_letters = []
    global guessed_words_count

    # определяем сложность
    if complexity == 1:
        # отрисовка слова с первой и последней буквой и их повторениями внутри слова
        word_completion = "".join([i if i == word[0] or i == word[-1] else "_" for i in word])
        # создаём список с отрисованными буквами для последующих проверок
        used_letters = [i for i in word_completion if i.isalpha()]
    else:
        word_completion = '_' * len(word)

    print("Я загадал слово... ;)")

    # первая отрисовка виселицы и жизней
    print(display_hangman(tries))
    print()
    print(f"Количество ваших жизней равно {tries} ")
    print()

    print(f"Попробуйте угадать это слово: {word_completion}")

    # сам цикл игры
    while True:
        while True:  # ввод буквы или слова
            clue = input("Введи букву или целое слово: ")
            if clue in used_letters:
                print("Эта буква уже была отрисована при генерации слова! Попробуйте ещё раз, жизнь не забираю!")
                print()
                continue
            if clue in guessed_letters or clue in guessed_words:  # проверка, не была ли введена буква ранее
                print("Вы уже вводили это ранее! Попробуйте ещё раз, так и быть - не отнимаю жизнь!")
                print()
                continue
            if not clue.isalpha():  # проверка, вдруг введена буква или слово
                print("Вы ввели не букву или слово, попробуйте ещё раз!")
                print()
                continue
            else:
                if len(clue) == 1:
                    guessed_letters.append(clue)  # помещаем букву в список введённых ранее букв
                    break
                else:
                    guessed_words.append(clue)  # помещаем слово в список введённых ранее слов
                    break
        if len(clue) > 1:
            if clue.lower() == word:  # проверка, правильное ли было введено слово
                print()
                print(f"Вы угадали слово \"{word}\"! Вы - настоящий марксист! В ГУЛАГ вас или расстрелять?")
                print(f"Directed by Robert B. Weide")
                guessed_words_count += 1
                break
            else:
                tries -= 1
                if tries == 0:  # проверка, есть ли возможные попытки
                    print(display_hangman(tries))
                    print(f"Вы либерал, и вы повешены! Вы не отгадали настоящее марксистское слово \"{word}\"!")
                    break
                print(f"Я загадал не слово \"{clue}\"! Количество ваших жизней равняется {tries}.")
                if tries >= 3:  # добавляем психологическое давление в процесс отгадывания
                    print("Осторожнее! Так и висящим либералом можно стать!")
                elif 0 < tries < 3:
                    print("Вы что, либерал??? Уже почти на виселице!")
                print(display_hangman(tries))
                if guessed_letters:  # если ранее не вводились буквы, они отрисовываться не будут
                    print(f"Буквы, которые вы называли: {guessed_letters}")
                if guessed_words:  # если ранее не вводились слова, они отрисовываться не будут
                    print(f"Слова, которые вы называли: {guessed_words}")
                print(f"Слово: {word_completion}")
                continue
        else:
            if clue.lower() not in word:  # проверка, входит ли буква в слово
                tries -= 1
                if tries == 0:  # проверка, есть ли возможные попытки
                    print(display_hangman(tries))
                    print(f"Вы либерал, и вы повешены! Вы не отгадали настоящее марксистское слово \"{word}\"!")
                    break
                print(f"Буквы \"{clue}\" нет в загаданном слове! Количество ваших жизней равняется {tries}.")
                if tries >= 3:
                    print("Осторожнее! Так и висящим либералом можно стать!")
                elif 0 < tries < 3:
                    print("Вы что, либерал??? Уже почти на виселице!")
                print(display_hangman(tries))
                if guessed_letters:
                    print(f"Буквы, которые вы называли: {guessed_letters}")
                if guessed_words:
                    print(f"Слова, которые вы называли: {guessed_words}")
                print(f"Слово: {word_completion}")
                continue
            else:
                word_completion_inner = ""
                for i in range(len(word)):  # перерисовка слова с учётом правильно введённой буквы
                    if word[i] == clue:
                        word_completion_inner += clue
                    else:
                        word_completion_inner += word_completion[i]
                word_completion = word_completion_inner
                if "_" not in word_completion:  # проверка, все ли буквы были отгаданы
                    print()
                    print(f"Вы угадали все буквы в слове \"{word}\"! Настоящий марксист! В ГУЛАГ вас или расстрелять?")
                    print(f"Directed by Robert B. Weide")
                    guessed_words_count += 1
                    break
                print(f"Буква \"{clue}\" есть в загаданном слове!")
                if word_completion.count("_") > len(word) / 2:  # добавляем чуть разнообразия в процесс отгадывания
                    print("Вы на шаг ближе к тому, чтобы я назвал вас настоящим марксистом!")
                elif word_completion.count("_") == 2:
                    print("ВЫ ПОЧТИ-ПОЧТИ марксист в моих глазах! Ещё немного! Две буквы!")
                elif word_completion.count("_") == 1:
                    print("ЕЩЁ ВСЕГО ОДНА БУКВА, ТОВАРИЩ!")
                else:
                    print("Вы КРАЙНЕ БЛИЗКИ к тому, чтобы я признал вас НАСТОЯЩИМ марксистом!")
                print()
                if guessed_letters:
                    print(f"Буквы, которые вы называли: {guessed_letters}")
                if guessed_words:
                    print(f"Слова, которые вы называли: {guessed_words}")
                print(f"Слово: {word_completion}")


# функция, отвечающая за начало игры, выбор сложности, повторения, конец
def play():
    print("Давай угадывать слова!")
    while True:
        while True:
            mode = input("Какой уровень сложности вы выберете? 1 - либерал (легко), 2 - марксист (сложно): ")
            if mode not in "12" or mode == "12":
                print("Вы ввели что-то не то, попробуйте снова.")
                continue
            else:
                mode = int(mode)
                break

        game(get_word(), mode)  # вызываем функцию игры, генерируем слово, указываем сложность

        if not word_list:  # ну, а вдруг слова в списке закончатся?
            print()
            print("Вы отгадали все имеющиеся слова, вы не просто марксист, вы ГИГА-МАРКСИСТ! Спасибо!")
            print(f"Количество отгаданных вами за этот заход марксистских терминов равно {guessed_words_count} (все!)")
            print()
            print("Made by a convinced liberal with huge self-irony")

        while True:  # возможный перезапуск игры
            print()
            play_choice = input("Сыграем ещё? 1 - да, 2 - нет: ")
            if play_choice not in "12" or play_choice == "12":
                print("Вы ввели что-то не то, попробуйте снова.")
                continue
            else:
                play_choice = int(play_choice)
                break

        if play_choice == 1:
            print()
            print("Хорошо, товарищ, сыграем ещё!")
            print(f"Количество отгаданных вами за этот заход марксистских терминов равно {guessed_words_count}.")
            print()
        else:
            print()
            print("Хорошо вам отдохнуть на Колыме, товарищ!")
            print(f"Количество отгаданных вами за этот заход марксистских терминов равно {guessed_words_count}.")
            print()
            print("Made by a convinced liberal with huge self-irony")
            break


play()  # вызываем функцию игры:)
