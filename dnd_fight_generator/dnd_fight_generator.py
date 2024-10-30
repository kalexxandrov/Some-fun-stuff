import random as rng


class Zombie:
    def __init__(self) -> None:
        self.species = 'Зомби [обычный]'
        self.base_hit_points = 22
        self.current_hit_points = 22
        self.armor_class = 8
        self.strength = (13, 1)
        self.dexterity = (6, -2)
        self.constitution = (16, 3)
        self.intelligence = (3, -4)
        self.wisdom = (6, -2)
        self.charisma = (5, -3)
        self.accuracy_bonus = 3
        self.max_damage = 7

    def initiative_roll(self) -> int:
        self.initiative = rng.randint(1, 20)
        if self.initiative == 1:
            return 0
        elif self.initiative == 20:
            return 100
        else:
            self.initiative += self.dexterity[1]
            return self.initiative

    def attack(self) -> int:
        return rng.randint(1, 6) + 1

    def undead_resistance(self, damage: int) -> bool:
        return rng.randint(1, 20) > 5 + damage

    def take_damage(self, damage: int) -> int:
        self.current_hit_points -= damage
        if self.current_hit_points <= 0:
            if self.undead_resistance(damage):
                self.current_hit_points = 1
            else:
                self.current_hit_points = 0
        return self.current_hit_points


class HugeZombie:
    def __init__(self) -> None:
        self.species = 'Зомби [огромный]'
        self.base_hit_points = 85
        self.current_hit_points = 85
        self.armor_class = 8
        self.strength = (19, 4)
        self.dexterity = (6, -2)
        self.constitution = (18, 4)
        self.intelligence = (3, -4)
        self.wisdom = (6, -2)
        self.charisma = (5, -3)
        self.accuracy_bonus = 6
        self.max_damage = 18

    def initiative_roll(self) -> int:
        self.initiative = rng.randint(1, 20)
        if self.initiative == 1:
            return 0
        elif self.initiative == 20:
            return 100
        else:
            self.initiative += self.dexterity[1]
            return self.initiative

    def attack(self) -> int:
        return sum([rng.randint(1, 8) for _ in range(2)]) + 2

    def undead_resistance(self, damage: int) -> bool:
        return rng.randint(1, 20) > 5 + damage

    def take_damage(self, damage: int) -> int:
        self.current_hit_points -= damage
        if self.current_hit_points <= 0:
            if self.undead_resistance(damage):
                self.current_hit_points = 1
            else:
                self.current_hit_points = 0
        return self.current_hit_points


def create_creatures() -> None:
    while True:
        while True:
            try:
                print('\033[1m' + 'Выберите тип существ: ' + '\033[0m')
                print('1 - Зомби [обычный].')
                print('2 - Зомби [огромный].')
                print()
                species = int(input('\033[1m' + 'Введите число: ' + '\033[0m'))
                print()
            except ValueError:
                print('Вы ввели что-то не то, попробуйте снова!')
                print()
                continue
            else:
                if species not in all_species:
                    print('Вы ввели неверное число. Попробуйте снова!')
                    print()
                    continue
                break
        while True:
            try:
                n = int(input('\033[1m' + 'Введите количество существ '
                              'выбранного типа: ' + '\033[0m'))
                print()
            except ValueError:
                print('Вы ввели что-то не то, попробуйте снова!')
                print()
                continue
            else:
                for _ in range(n):
                    creatures.append(all_species[species]())
                break
        while True:
            try:
                print('\033[1m' + 'Хотите добавить ещё существ для '
                      'боя?' + '\033[0m')
                print('1 - Да.')
                print('2 - Нет.')
                print()
                flag = int(input('\033[1m' + 'Введите число: ' + '\033[0m'))
                print()
            except ValueError:
                print('Вы ввели что-то не то, попробуйте снова!')
                continue
            else:
                if flag not in (1, 2):
                    print('Вы ввели неверное число. Попробуйте снова!')
                    continue
                break
        if flag == 2:
            break


def mass_initiative_roll() -> None:
    for i in range(len(creatures)):
        print(f'Инициатива существа {i + 1} ({creatures[i].species}): '
              f'{creatures[i].initiative_roll()}.')


def statuses_check() -> bool:
    alive = False
    print('\033[1m' + 'Живые враги: ' + '\033[0m')
    for i in range(len(creatures)):
        if creatures[i].current_hit_points > 0:
            alive = True
            print(f'Существо {i + 1} ({creatures[i].species}) - '
                  f'{creatures[i].current_hit_points} хп.')
    return alive


def status_check(creature) -> bool:
    return creature.current_hit_points > 0


def accuracy_check(creature, armor_class: int) -> bool:
    roll = rng.randint(1, 20)
    if roll == 1:
        return 1
    elif roll == 20:
        return 20
    elif roll + creature.accuracy_bonus > armor_class:
        return 'hit'
    else:
        return 'miss'


def take_attack(creature):
    while True:
        try:
            armor_class = int(input('\033[1m' + 'Введите КБ '
                                    'цели атаки: ' + '\033[0m'))
        except ValueError:
            print('Вы ввели что-то не то, попробуйте снова!')
            print()
            continue
        else:
            break
    accuracy = accuracy_check(creature, armor_class)
    if accuracy == 1:
        print('Критический промах!')
    elif accuracy == 20:
        print(f'Критический успех! Существо {pick} ({creature.species}) '
              f'нанесло урон в размере {creature.max_damage}!')
    elif accuracy == 'hit':
        damage = creature.attack()
        print(f'Существо {pick} ({creature.species}) '
              f'нанесло урон в размере {damage}.')
    else:
        print(f'Существо {pick} ({creature.species}) промахнулось.')


def attack_the_creature(creature) -> None:
    while True:
        try:
            damage = int(input('\033[1m' + 'Введите нанесённый '
                               'урон: ' + '\033[0m'))
        except ValueError:
            print('Вы ввели что-то не то, попробуйте снова!')
            print()
            continue
        else:
            break
    hp_left = creature.take_damage(damage)
    if not hp_left:
        print('И это летал!')
    else:
        max_hp = creature.base_hit_points
        print(f'У существа {pick} ({creature.species}) '
              f'осталось {hp_left} хп из {max_hp}.')


def is_wise(creature) -> bool:
    wisdom_check = rng.randint(1, 20) > 13
    if wisdom_check:
        print(f'Существо {pick} ({creature.species}) прошло проверку '
              'на мудрость! Существо мудро!')
    else:
        print(f'Существо {pick} ({creature.species}) не прошло проверку '
              'на мудрость. Существо не мудро.')
        print()
        attack_the_creature(creatures[pick - 1])


def start_fight():
    while True:
        global pick
        print()
        if not statuses_check():
            print('Все враги мертвы, драка закончена!')
            break
        print()
        try:
            pick = int(input('\033[1m' + 'Выбрать существо: ' + '\033[0m'))
        except ValueError:
            print('Вы ввели что-то не то, попробуйте заново!')
            continue
        print()
        if not status_check(creatures[pick - 1]):
            print(f'Существо {pick} ({creatures[pick - 1].species}) уже '
                  'мертво, выберите другое!')
            continue
        while True:
            try:
                print('\033[1m' + 'Что сделать?' + '\033[0m')
                print('1 - атаковать.')
                print('2 - получить урон.')
                print('3 - проверка на мудрость.')
                print('0 - выйти.')
                print()
                action = int(input('\033[1m' + 'Введите число: ' + '\033[0m'))
            except ValueError:
                print('Вы ввели что-то не то, попробуйте заново!')
                print()
                continue
            else:
                break
        print()
        if action == 1:
            attack_the_creature(creatures[pick - 1])
        elif action == 2:
            take_attack(creatures[pick - 1])
        elif action == 3:
            is_wise(creatures[pick - 1])
        elif action == 0:
            print('Экстренный выход из программы!')
            break
        else:
            print('Вы ввели что-то не то, попробуйте снова!')


all_species = {1: Zombie, 2: HugeZombie}
creatures = []

create_creatures()
mass_initiative_roll()
start_fight()
