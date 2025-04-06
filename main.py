# Part of case-study #3
# Case has been done by Mihail Gordeev and Sergey Chirkov

import random
import math
import events as ev

planet_systems = [33, 33, 33]
money = [100, 100, 100]
population = [1000, 1000, 1000]
materials = [1000, 1000, 1000]
oil = [20000, 20000, 20000]
food = [300000, 300000, 300000]
min_stations = [[14, 3, 3], [14, 3, 3], [14, 3, 3]]
#List of lists: lots[0] - food station, lots[1] - material station, lots[2] - oil station
ships = [[5, 0, 0], [5, 0, 0], [5, 0, 0]]
#List of lists: lots[0] - fighter jet, lots[1] - bomber, lots[2] - corvette
count_teams = 3
lots = []
#List of lists: lots[0] - type of product, lots[1] - name of sails, lots[2] - value of product, lots[3] - price

name_lots = {'oil': 'Топливо',
             'materials': 'Материалы',
             'food': 'Еда'}

dict_name_station = {0: 'продовольственных', 1: 'материало-добывающих', 2: 'топливо-добывающих'}
teams = {}


def start(teams):
    '''
    function - start screen for everyone
    '''

    teams[0] = input('Введите название первой команды ')
    teams[1] = input('Введите название второй команды ')
    teams[2] = input('Введите название третьей команды ')
    print('=================================')
    print('Вы - император космических земель',
          'Ваша миссия - контроль 80 планетарных систем или накопление 50000 '
          'материала и удержание до своего следующего хода',
          'У каждого из вас сейчас:',
          '33 планетарных систем',
          '1000 единиц населения'
          '300000 единиц продовольствия',
          '20000 единиц топлива',
          '1000 единиц материала',
          '100 денежных единиц',
          '20 добывающих станций:',
          ' 14 для продовольствия',
          ' 3 для материалов',
          ' 3 для топлива',
          '5 истребителей', sep='\n')
    print('=================================')


def check_victory(planet_systems, materials, count_teams):
    '''
    function for checking victory status if teams

    :param planet_systems:
    :param materials:
    :param count_teams:
    :return:
    '''


    if max(planet_systems) >= 80 or max(materials) >= 55000 or count_teams == 1:
        return True
    return False


def check_loss(planet_systems, population):
    '''
    function for checking lose status if teams

    :param planet_systems:
    :param population:
    :return:
    '''


    global teams
    for team in teams:
        if planet_systems[team] <= 0 or population[team] <= 0:
            print(f'Команда {teams[team]} проиграла!')
            del teams[team]
            return True
    return False


def event(team):
    '''
    function for randomize event from another 'events.py' file

    :param team:
    :return:
    '''


    global planet_systems, money, population, materials, oil, food, min_stations
    list_events = ['ev.oli_down_ev(oil, team)',
                   'ev.oli_down_ev1(oil, team)',
                   'ev.oli_up_ev(oil, team)',
                   'ev.oli_up_ev1(oil, team)',
                   'ev.food_up_ev(food, team)',
                   'ev.food_up_ev1(food, team)',
                   'ev.food_down_ev(food, team)',
                   'ev.food_down_ev1(food, team)',
                   'ev.population_up_ev(population, team)',
                   'ev.population_up_ev1(population, team)',
                   'ev.population_down_ev(population, team)',
                   'ev.population_down_ev1(population, team)',
                   'ev.money_up_ev(money, team)',
                   'ev.money_up_ev1(money, team)',
                   'ev.money_up_ev2(money, team)',
                   'ev.money_down_ev(money, team)',
                   'ev.money_down_ev1(money, team)',
                   'ev.money_down_ev2(money, team)',
                   'ev.planet_systems_up_ev(planet_systems, team)',
                   'ev.planet_systems_up_ev1(planet_systems, team)',
                   'ev.planet_systems_up_ev2(planet_systems, team)',
                   'ev.planet_systems_down_ev(planet_systems, team)',
                   'ev.planet_systems_down_ev1(planet_systems, team)',
                   'ev.planet_systems_down_ev2(planet_systems, team)',
                   'ev.planet_systems_down_ev3(planet_systems, team)',
                   'ev.materials_down_ev(materials, team)',
                   'ev.materials_down_ev1(materials, team)',
                   'ev.materials_down_ev2(materials, team)',
                   'ev.materials_up_ev(materials, team)',
                   'ev.materials_up_ev1(materials, team)',
                   'ev.materials_up_ev2(materials, team)',
                   'ev.mat_station_up_ev(min_stations, team)',
                   'ev.mat_station_down_ev(min_stations, team)',
                   'ev.prod_station_up_ev(min_stations, team)',
                   'ev.prod_station_down_ev(min_stations, team)',
                   'ev.oil_station_up_ev(min_stations, team)',
                   'ev.oil_station_down_ev(min_stations, team)']
    exec(random.choice(list_events))


def income(team):
    '''
    function for counting income from mining station

    :param team:
    :return:
    '''


    materials[team] += 750 * min_stations[team][1]
    food[team] += 16000 * min_stations[team][0]
    oil[team] += 6000 * min_stations[team][2]


def costs(team):
    '''
    function for counting costs for every step for everyone

    :param team:
    :return:
    '''


    global planet_systems, money, population, materials, oil, food, min_stations

    food[team] = int(food[team] - population[team] * 250)
    if food[team] < 0:
        print(f'Император, у вас нехватка продовольствия в размере {abs(food[team])}.',
              f'Погибло {math.ceil(abs(food[team]) / 250)} населения, запасы продовольствия истощены.', sep='\n')
        population[team] -= math.ceil(abs(food[team]) / 250)
        food[team] = 0

    oil[team] -= (min_stations[team][0] + min_stations[team][1] + min_stations[team][2]) * 500
    if oil[team] < 0:
        destroyed_station = random.choice(list(dict_name_station))
        print(f'Император, у вас нехватка топлива для обеспечения исправной работы добывающих станций',
              f'Выведено из строя {math.ceil(abs(oil[team]) / 500)} {dict_name_station[destroyed_station]}'
              'рабочих станций, запасы топлива истощены.',
              sep='\n')
        min_stations[team][destroyed_station] -= math.ceil(abs(oil[team]) / 500)
        oil[team] = 0

    dif_actual_and_required_population = population[team] - (
                min_stations[team][0] + min_stations[team][1] + min_stations[team][2]) * 20
    if dif_actual_and_required_population < 0:
        destroyed_station = random.choice(list(dict_name_station))
        print(f'Император, у вас нехватка населения для обеспечения исправной работы добывающих станций',
              f'Выведено из строя {math.ceil(abs(dif_actual_and_required_population) / 20)} '
              f'{dict_name_station[destroyed_station]} рабочих станций.',
              sep='\n')
        min_stations[team][destroyed_station] -= math.ceil(abs(oil[team]) / 20)

    if population[team] > planet_systems[team] * 100:
        dead = population[team] - planet_systems[team] * 100
        population[team] -= dead
        print('Император, ваши планеты перенаселены, люди умирают. ',
              f'Погибло {dead} населения.')


def indicators(team):
    '''
    function for printing all staff in one team

    :param team:
    :return:
    '''


    global planet_systems, money, population, materials, oil, food, min_stations

    planet_systems[team] = int(planet_systems[team])
    money[team] = int(money[team])
    population[team] = int(population[team])
    materials[team] = int(materials[team])
    oil[team] = int(oil[team])
    food[team] = int(food[team])

    q_min_stations = sum(min_stations[team])
    print('Император, представляем к вашему вниманию последние экономические '
          'показатели:',
          f'В вашем распоряжении находится {planet_systems[team]} планетарных систем',
          f'Величина населения составляет {population[team]} единиц',
          f'В вашей казне {money[team]} денежных единиц',
          f'На ваших складах скопилось {materials[team]} единиц материала',
          f'На ваших складах находится {oil[team]} единиц топлива',
          f'На ваших складах находится {food[team]} единиц продовольствия',
          f'В вашем распоряжении находится {min_stations[team][0]} '
          'продовольственных рабочих станций',
          f'В вашем распоряжении находится {min_stations[team][1]} '
          'материало-добывающих рабочих станций',
          f'В вашем распоряжении находится {min_stations[team][2]} '
          'топливо-добывающих рабочих станций',
          'Вы можете построить еще '
          f'{int(population[team] // 20 - q_min_stations)} рабочих станций',
          sep='\n')


def trade(team):
    '''
    function for trading with space union federation

    :param team:
    :return:
    '''


    indict = 2
    while indict != 1 and indict != 0:
        try:
            indict = int(input('Вы хотите торговать с галактической федерацией? '
                               '1 - да, 0 - нет '))
        except:
            continue

    match indict:
        case 1:
            print('Что вы хотите купить? ')
            purse = int(input('1 - еда, 2 - топливо, 3 - материалы, 0 - выйти из меню '))
            match purse:
                case 0:
                    pass
                case 1:
                    price = (population[team] ** 2) / 500000
                    q = int(input(f'Цена ед. еды - {price}. '
                                  f'Сколько единиц еды вы хотите приобрести? '))
                    print(f'Цена {q} единиц еды - {q * price}. '
                          f'У вас на балансе {money[team]}')
                    des = int(input(f'Покупаем? {q} ед. еды?'
                                    '1 - да, 0 - нет'))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] >= price*q:
                                food[team] += q
                                money[team] -= price*q
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
                case 2:
                    price = random.randint(20, 50)/100
                    q = int(input(f'Цена ед. топлива - {price}. '
                                  f'Сколько единиц топлива вы хотите приобрести? '))
                    print(f'Цена {q} единиц топлива - {price*q}. '
                          f'У вас на балансе {money[team]}')
                    des = int(input(f'Покупаем? {q} ед. топлива? '
                                    '1 - да, 0 - нет '))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] >= price*q:
                                oil[team] += q
                                money[team] -= price*q
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
                case 3:
                    price = random.randint(80, 120)/5000
                    q = int(input(f'Цена ед. материала - {price}. '
                                  f'Сколько единиц материала вы хотите приобрести? '))
                    des = int(input(f'Покупаем? {q} материала? '
                                    '1 - да, 0 - нет '))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] >= price*q:
                                materials[team] += q
                                money[team] -= price*q
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
        case 0:
            pass


def lot_given(team):
    '''
    function for trading on stock between players

    :param team:
    :return:
    '''


    indict = 2
    while indict != 1 and indict != 0:
        try:
            indict = int(input('Вы хотите что-то продать на бирже? '
                               '1 - да, 0 - нет '))
        except:
            continue
    match indict:
        case 0:
            pass
        case 1:
            print(f'Сейчас на бирже такие лоты: ')
            for i in lots:
                print(name_lots[i[0]], f' Колличество - {i[2]}, цена лота - {i[3]}')
            mat = int(input('Что конкретно вы хотите продать?'
                            '1 - еду, 2 - топливо, 3 - материалы, 0 - выйти из меню'))
            match mat:
                case 0:
                    pass
                case 1:
                    print(f'У вас сейчас {food[team]} еды')
                    q = int(input('Сколько еды вы готовы продать? -->'))
                    if q <= food[team]:
                        price = int(input(f'За сколько вы готовы продать {q} еды?'))
                        lots.append(['food', team, q, price])
                        food[team] -= q
                        print(f'Вы выставили лот с едой ({q} ед.) за {price}')
                    else:
                        print('У вас недостаточно еды')
                case 2:
                    print(f'У вас сейчас {oil[team]} топлива')
                    q = int(input('Сколько топлива вы готовы продать? -->'))
                    if q <= oil[team]:
                        price = int(input(f'За сколько вы готовы продать {q} топлива?'))
                        lots.append(['oil', team, q, price])
                        oil[team] -= q
                        print(f'Вы выставили лот с топливом ({q} ед.) за {price}')
                    else:
                        print('У вас недостаточно топлива')
                case 3:
                    print(f'У вас сейчас {materials[team]} материала')
                    q = int(input('Сколько материала вы готовы продать? -->'))
                    if q <= materials[team]:
                        price = int(input(f'За сколько вы готовы продать {q} материала?'))
                        lots.append(['materials', team, q, price])
                        materials[team] -= q
                        print(f'Вы выставили лот с материалом ({q} ед.) за {price}')
                    else:
                        print('У вас недостаточно материалов')


def lot_taking (team):
    '''
    function for trading on stock between players

    :param team:
    :return:
    '''


    indict = 2
    while indict != 1 and indict != 0:
        try:
            indict = int(input('Вы хотите что-то купить на бирже?'
                               '1 - да, 0 - нет '))
        except:
            continue
    match indict:
        case 0:
            pass
        case 1:
            print(f'Сейчас на бирже такие лоты:')
            for i in lots:
                print(name_lots[i[0]], f' Колличество - {i[2]}, цена лота - {i[3]}')
            mat = int(input('Что конкретно вы хотите купить?'
                            '1 - еду, 2 - топливо, 3 - материалы, 0 - выйти из меню'))
            match mat:
                case 0:
                    pass
                case 1:
                    print(f'У вас сейчас {food[team]} еды')
                    k = 0
                    lot_buy = {}
                    for i in lots:
                        if i[0] == 'food':
                            print(f'Лот {k}, Количество - {i[2]}, цена лота - {i[3]}')
                            lot_buy[k] = i
                            k +=1
                    l = int(input('Какой лот вы готовы купить? -->'))
                    if lot_buy[l][3] <= money[team]:
                        food[team] += lot_buy[l][2]
                        money[team] -= lot_buy[l][3]
                        money[lot_buy[l][1]] += lot_buy[l][3]
                        lots.remove(lot_buy[l])
                        print('Вы купили лот с едой, поздравляем!')
                    else:
                        print('У вас недостаточно денег для покупки лота')
                case 2:
                    print(f'У вас сейчас {oil[team]} топлива')
                    k = 0
                    lot_buy = {}
                    for i in lots:
                        if i[0] == oil:
                            print(f'Лот {k}, Количество - {i[2]}, цена лота - {i[3]}')
                            lot_buy[k] = i
                            k += 1
                    l = int(input('Какой лот вы готовы купить? -->'))
                    if lot_buy[l][3] <= money[team]:
                        oil[team] += lot_buy[l][2]
                        money[team] -= lot_buy[l][3]
                        money[lot_buy[l][1]] += lot_buy[l][3]
                        lots.remove(lot_buy[l])
                        print('Вы купили лот с топливом, поздравляем!')
                    else:
                        print('У вас недостаточно денег для покупки лота')
                case 3:
                    print(f'У вас сейчас {materials[team]} материалов')
                    k = 0
                    lot_buy = {}
                    for i in lots:
                        if i[0] == materials:
                            print(f'Лот {k}, Количество - {i[2]}, цена лота - {i[3]}')
                            lot_buy[k] = i
                            k += 1
                    l = int(input('Какой лот вы готовы купить? -->'))
                    if lot_buy[l][3] <= money[team]:
                        materials[team] += lot_buy[k][2]
                        money[team] -= lot_buy[l][3]
                        money[lot_buy[l][1]] += lot_buy[l][3]
                        lots.remove(lot_buy[k])
                        print('Вы купили лот с материалами, поздравляем!')
                    else:
                        print('У вас недостаточно денег для покупки лота')


def build(team):
    '''
    function for building army and mining station

    :param team:
    :return:
    '''


    indict = 2
    while indict != 1 and indict != 0:
        try:
            indict = int(input('Вы хотите построить что-нибудь '
                               '1 - да, 0 - нет '))
        except:
            continue

    match indict:
        case 0:
            pass
        case 1:
            indict = int(input('Что вы хотите построить? '
                               '1 - добывающие станции, 2 - боевые корабли, 0 - выйти из меню '))
            match indict:
                case 0:
                    pass

                case 1:
                    indict = int(input('Какую станцию вы хотите построить? '
                                       '1 - материало-добывающие, 2 - продовольствие-добывающие, '
                                       '3 - топливо-добывающие, 0 - выйти из меню '))
                    match indict:
                        case 0:
                            pass

                        case 1:
                            print('Каждая станция требует 1000 материала на постройку '
                                  f'У вас сейчас {materials[team]} материала ')
                            q = 6
                            while q > 5:
                                try:
                                    q = int(input('Сколько материало-добывающих станций вы хотите построить? '))
                                except:
                                    print('Максимальное количество станций, построенных за один ход - 5')
                                    continue
                            if materials[team] >= q*1000:
                                materials[team] -= q*1000
                                min_stations[team][1] += q
                                print(f'Поздравляем с постройкой {q} материальных станций')
                                indicators(team)
                            else:
                                print('У Вас недостаточно материала')

                        case 2:
                            print('Каждая станция требует 1000 материала'
                                f'У вас сейчас {materials[team]} материала')
                            q = 6
                            while q > 5:
                                try:
                                    q = int(input('Сколько продовольственных станций вы хотите построить? '))
                                except:
                                    print('Максимальное количество станций, построенных за один ход - 5')
                                    continue
                            if materials[team] >= q * 1000:
                                materials[team] -= q * 1000
                                min_stations[team][0] += q
                                print(f'Поздравляем с постройкой {q} продовольственных станций')
                                indicators(team)
                            else:
                                print('У Вас недостаточно материала')

                        case 3:
                            print('Каждая станция требует 1000 материала'
                                f'У вас сейчас {materials[team]} материала')
                            q = 6
                            while q > 5:
                                try:
                                    q = int(input('Сколько топливных станций вы хотите построить? '))
                                except:
                                    print('Максимальное количество станций, построенных за один ход - 5')
                                    continue
                            if materials[team] >= q * 1000:
                                min_stations[team][2] += q
                                print(f'Поздравляем с постройкой {q} топливных станций')
                                indicators(team)
                            else:
                                print('У Вас недостаточно материала')

                case 2:
                    indict = int(input('Какой корабль вы хотите построить?\n'
                                       '1 - истребитель, 2 - бомбардировщик,'
                                       '3 - линкор, 0 - выйти из меню'))
                    match indict:
                        case 0:
                            pass

                        case 1:
                            print('Каждый истребитель требует 100 материала'
                                 f'У вас сейчас {materials[team]} материала')
                            q = 101
                            while q > 100:
                                try:
                                    q = int(input('Сколько истребителей вы хотите построить?'))
                                except:
                                    print('Максимальное количество истребителей, построенных за один ход - 100')
                                    continue
                            if materials[team] >= q * 100:
                                materials[team] -= 100*q
                                ships[team][0] += q
                                print(f'Поздравляем с постройкой {q} истребителей')
                                indicators(team)
                            else:
                                print('У Вас недостаточно материалов')

                        case 2:
                            print('Каждый бомбардировщик требует 100 материала'
                                 f'У вас сейчас {materials[team]} материала')
                            q = 101
                            while q > 100:
                                try:
                                    q = int(input('Сколько бомбардировщиков вы хотите построить?'))
                                except:
                                    print('Максимальное количество бомбардировщиков, построенных за один ход - 100')
                                    continue
                            if materials[team] >= q * 100:
                                materials[team] -= 100 * q
                                ships[team][1] += q
                                print(f'Поздравляем с постройкой {q} бомбардировщиков')
                                indicators(team)
                            else:
                                print('У Вас не хватает материалов')

                        case 3:
                            print('Каждый корвет требует 150 материала'
                                  f'У вас сейчас {materials[team]} материала')
                            q = 76
                            while q > 75:
                                try:
                                    q = int(input('Сколько корветов вы хотите построить?'))
                                except:
                                    print('Максимальное количество корветов, построенных за один ход - 75')
                                    continue
                            if materials[team] >= q * 150:
                                materials[team] -= 150 * q
                                ships[team][2] += q
                                print(f'Поздравляем с постройкой {q} корветов')
                                indicators(team)
                            else:
                                print('У Вас не хватает материалов')


def battle(team, opponent):
    '''
    function for fighting between teams

    :param team:
    :param opponent:
    :return:
    '''


    global ships, planet_systems, oil
    attacker = team
    defender = opponent

    input('Вы хотите продолжить? ')
    print('=================================')

    print('Император, в вашем распоряжении:',
          f'{ships[team][0]} истребителей',
          f'{ships[team][1]} бомбардировщиков',
          f'{ships[team][2]} корветов', sep='\n')

    jet, bomber, corvette = 10000, 10000, 10000

    while ships[team][0] < jet and ships[team][1] < bomber and ships[team][2] < corvette:
        print('Сколько истребителей, '
              'бомбардировщиков и корветов вы отправите на захват?\n'
              'Укажите требуемые значения, каждое в новой строке.')

        try:
            jet = int(input('Сколько истребителей? '))
            bomber = int(input('Сколько бомбардировщиков? '))
            corvette = int(input('Сколько корветов? '))
        except:
            print('Император, введите корректное значение!')
            continue

    attack_ships = [jet, bomber, corvette]

    area = 0
    while area == 0:
        try:
            area = int(input(('Введите размер территории для захвата, '
                              f'не больше чем {planet_systems[opponent]} ')))
            if oil[team] < area * 2000:
                print('Император, у нас недостаточно топлива для таких расстояний. ',
                      f'Нехватка составляет {area * 2500 - oil[team]}')
                return
            oil[team] -= area * 2000
        except:
            continue
    p_area = math.ceil(planet_systems[opponent] / area)

    defend_ships = list(map(lambda x: math.ceil(x / p_area), ships[opponent]))

    j1, b1, c1 = attack_ships[0], attack_ships[1], attack_ships[2]
    j2, b2, c2 = defend_ships[0], defend_ships[1], defend_ships[2]

    j1_u, b1_u, c1_u = j1, b1, c1
    j2_u, b2_u, c2_u = j2, b2, c2
    j1_o, b1_o, c1_o = ships[team][0], ships[team][1], ships[team][2]
    j2_o, b2_o, c2_o = ships[opponent][0], ships[opponent][1], ships[opponent][2]

    n = 1
    while abs(j1) + abs(b1) + abs(c1) > 0 and abs(j2) + abs(b2) + abs(c2) > 0:
        print('=================================')

        print(f'{n} раунд.',
              f'Число кораблей команды {teams[attacker]}:',
              f'{j1} истребителей, {b1} бомбардировщиков, {c1} корветов',
              f'Число кораблей команды {teams[defender]}:',
              f'{j2} истребителей, {b2} бомбардировщиков, {c2} корветов',
              f'Атакует команда {teams[attacker]}', sep='\n')

        if j1 == 0 and b1 == 0 and j2 == 0 and b2 == 0:
            c2 -= c1
        elif j1 == 0 and c1 == 0 and b2 == 0 and c2 == 0:
            b2 -= b1
        elif b1 == 0 and c1 == 0 and b2 == 0 and c2 == 0:
            j2 -= j1

        if j2 > 0 and b2 > 0 and c2 > 0:
            j2 = 0 if (j2 - c1) < 0 else (j2 - c1)
            b2 = 0 if (b2 - j1) < 0 else (b2 - j1)
            c2 = 0 if (c2 - b1) < 0 else (c2 - b1)
        
        elif j2 == 0:
            b2 = 0 if (b2 - j1 - c1//2) < 0 else (b2 - j1 - c1//2)
            c2 = 0 if (c2 - b1 - c1//2) < 0 else (c2 - b1 - c1//2)
        
        elif b2 == 0:
            j2 = 0 if (j2 - c1 - j1//2) < 0 else (j2 - c1 - j1//2)
            c2 = 0 if (c2 - b1 - j1//2) < 0 else (c2 - b1 - j1//2)
        
        elif c2 == 0:
            j2 = 0 if (j2 - c1 - b1) < 0 else (j2 - c1 - b1)
            b2 = 0 if (b2 - j1 - b1) < 0 else (b2 - j1 - b1)

        attacker, defender = defender, attacker
        j1, j2 = j2, j1
        b1, b2 = b2, b1
        c1, c2 = c2, c1
        n += 1

    print('=================================')

    if j1 + b1 + c1 == 0 and n % 2 != 0:
        print(f'Победила команда {teams[opponent]}')
        ships[team] = [0, 0, 0]
        ships[opponent] = [j2_o - j2_u + j2,
                           b2_o - b2_u + b2,
                           c2_o - c2_u + c2]
        
    elif j1 + b1 + c1 == 0 and n % 2 == 0:
        print(f'Победила команда {teams[team]}')
        planet_systems[team] += area
        planet_systems[opponent] -= area
        ships[team] = [j1_o - j1_u,
                       b1_o - b1_u,
                       c1_o - c1_u]
        ships[opponent] = [j2_o - j2_u,
                           b2_o - b2_u,
                           c2_o - c2_u]
        
    elif j2 + b2 + c2 == 0 and n % 2 != 0:
        print(f'Победила команда {teams[team]}')
        planet_systems[team] += area
        planet_systems[opponent] -= area
        ships[team] = [j1_o - j1_u,
                       b1_o - b1_u,
                       c1_o - c1_u]
        ships[opponent] = [j2_o - j2_u,
                           b2_o - b2_u,
                           c2_o - c2_u]
        
    elif j2 + b2 + c2 == 0 and n % 2 == 0:
        print(f'Победила команда {teams[opponent]}')
        ships[team] = [0, 0, 0]
        ships[opponent] = [j2_o - j2_u + j1,
                           b2_o - b2_u + b1,
                           c2_o - c2_u + c1]


    print(f'Число кораблей команды {teams[team]}',
          f'{ships[team][0]} истребителей',
          f'{ships[team][1]} бомбардировщиков',
          f'{ships[team][2]} корветов', sep='\n')
    print(f'Число кораблей команды {teams[opponent]}',
          f'{ships[opponent][0]} истребителей',
          f'{ships[opponent][1]} бомбардировщиков',
          f'{ships[opponent][2]} корветов', sep='\n')


def battle_choose(team):
    '''
    additional function for fighting

    :param team:
    :return:
    '''


    battle_decree = 2
    while battle_decree != 1 and battle_decree != 0:
        try:
            battle_decree = int(input('Император, угодно ли вам начать боевые '
                                      'действия по захвату вражеской территории? '
                                      '1 - да, 0 - нет '))
        except:
            continue

    match battle_decree:
        case 1:
            match team:
                case 0:
                    opponent = int(input('На кого вы хотите напасть? '
                                         f'1 - команда {teams[1]}, '
                                         f'2 - команда {teams[2]} '))
                    battle(team, opponent)

                case 1:
                    opponent = int(input('На кого вы хотите напасть? '
                                         f'1 - команда {teams[0]}, '
                                         f'2 - команда {teams[2]} '))
                    battle(team, opponent)

                case 2:
                    opponent = int(input('На кого вы хотите напасть? '
                                         f'1 - команда {teams[0]}, '
                                         f'2 - команда {teams[1]} '))
                    battle(team, opponent)

        case 0:
            print('Как вам угодно')
            pass


def play(team):
    '''
    function with play mechanics

    :param team:
    :return:
    '''


    print(f'Играет команда {teams[team]}!')

    event(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    income(team)

    costs(team)

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    trade(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    lot_given(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    lot_taking(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    battle_choose(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    build(team)
    input('Вы хотите продолжить? ')
    print('=================================')


def main():
    global planet_systems, money, population, materials, oil, food, min_stations, teams, count_teams, lots, name_lots
    start(teams)

    count_revers = 0
    while check_victory(planet_systems, materials, count_teams) == False:
        for team in teams:
            play(team)
            if check_loss(planet_systems, population) == True:
                count_teams -= 1
                break

        if count_teams == 2 and count_revers == 0:
            count_revers += 1
            teams = dict(reversed(teams.items()))


    else:
        if planet_systems[0] >= 80:
            print(f'Выиграла команда {teams[0]}!')
        elif planet_systems[1] >= 80:
            print(f'Выиграла команда {teams[1]}!')
        elif planet_systems[2] >= 80:
            print(f'Выиграла команда {teams[2]}!')
        elif materials[0] >= 55000:
            print(f'Выиграла команда {teams[0]}!')
        elif materials[1] >= 55000:
            print(f'Выиграла команда {teams[1]}!')
        elif materials[2] >= 55000:
            print(f'Выиграла команда {teams[2]}!')
        elif teams.get(0) != None:
            print(f'Выиграла команда {teams[0]}!')
        elif teams.get(1) != None:
            print(f'Выиграла команда {teams[1]}!')
        elif teams.get(2) != None:
            print(f'Выиграла команда {teams[2]}!')


if __name__ == '__main__':
    main()
