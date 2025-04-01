import random
import math
import events as ev

planet_systems = [33, 33, 33]
money = [100, 100, 100]
population = [1000, 1000, 1000]
materials = [1000, 1000, 1000]
oil = [20000, 20000, 20000]
food = [300000, 300000, 300000]
min_stations = [[14, 3, 3], [14, 3, 3], [14, 3, 3]] #[Продовольственные, материальные, топливные]
ships = [[5, 0, 0], [5, 0, 0], [5, 0, 0]] #[Истребители, бомбардировщики, корветы]
count_teams = 3

dict_name_station = {0 : 'продовольственных', 1 : 'материало-добывающих', 2 : 'топливо-добывающих'}
teams = {}


def start(teams):
    teams[0] = input('Введите название первой команды ')
    teams[1] = input('Введите название второй команды ')
    teams[2] = input('Введите название третьей команды ')
    print('=================================')
    print('Вы - император космических земель',
          'Ваша миссия - контроль 80 планетарных систем или накопление 50000 материала и удержание до своего следующего хода',
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
          '5 истребителей', sep = '\n')
    print('=================================')


def check_victory(planet_systems, materials, count_teams):
    if max(planet_systems) >= 80 or max(materials) >= 55000 or count_teams == 1:
         return True
    return False


def check_loss(planet_systems, population):
    global teams
    for team in teams:
        if planet_systems[team] <= 0 or population[team] <= 0:
            print(f'Команда {teams[team]} проиграла!')
            del teams[team]
            return True
    return False


def event(team):
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
    materials[team] += 750 * min_stations[team][1]
    food[team] += 16000 * min_stations[team][0]
    oil[team] += 6000 * min_stations[team][2]

def costs(team):
    global planet_systems, money, population, materials, oil, food, min_stations

    food[team] = int(food[team] - population[team] * 250)
    if food[team] < 0:
        print(f'Император, у вас нехватка продовольствия в размере {abs(food[team])}.',
              f'Погибло {math.ceil(abs(food[team])/250)} населения, запасы продовольствия истощены.', sep = '\n')
        population[team] -= math.ceil(abs(food[team])/250)
        food[team] = 0

    oil[team] -= (min_stations[team][0] + min_stations[team][1] + min_stations[team][2]) * 500
    if oil[team] < 0:
        destroyed_station  = random.choice(list(dict_name_station))
        print(f'Император, у вас нехватка топлива для обеспечения исправной работы добывающих станций',
              f'Выведено из строя {math.ceil(abs(oil[team])/500)} {dict_name_station[destroyed_station]} рабочих станций, запасы топлива истощены.', sep = '\n')
        min_stations[team][destroyed_station] -= math.ceil(abs(oil[team])/500)
        oil[team] = 0

    dif_actual_and_required_population = population[team] - (min_stations[team][0] + min_stations[team][1] + min_stations[team][2]) * 20
    if dif_actual_and_required_population < 0:
        destroyed_station  = random.choice(list(dict_name_station))
        print(f'Император, у вас нехватка населения для обеспечения исправной работы добывающих станций',
              f'Выведено из строя {math.ceil(abs(dif_actual_and_required_population)/20)} {dict_name_station[destroyed_station]} рабочих станций.', sep = '\n')
        min_stations[team][destroyed_station] -= math.ceil(abs(oil[team])/20)


def indicators(team):
    global planet_systems, money, population, materials, oil, food, min_stations

    planet_systems[team] = int(planet_systems[team])
    money[team] = int(money[team])
    population[team] =int(population[team])
    materials[team] =int(materials[team])
    oil[team] = int(oil[team])
    food[team] =int(food[team])

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
          f'{int(population[team]//20 - q_min_stations)} рабочих станций', 
          sep = '\n')


def trade(team):
    indict = 2
    while indict != 1 and indict != 0:
        try:
            indict = int(input('Вы хотите торговать?'
                               '1 - да, 0 - нет '))
        except:
            continue

    match indict:
        case 1:
            print('Что вы хотите купить?')
            purse = int(input('1 - еда, 2 - топливо, 3 - материалы, 0 - выйти из меню'))
            match purse:
                case 0:
                    pass
                case 1:
                    price = (population[team]**2)/1000
                    print(f'Цена 500 единиц еды - {price}'
                          f'У вас на балансе {money[team]}')
                    des = int(input('Покупаем? 500 ед. еды?'
                                    '1 - да, 0 - нет'))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] <= price:
                                food[team] += 500
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
                case 2:
                    price = random.randint(20, 50)
                    print(f'Цена 100 единиц топлива - {price}'
                          f'У вас на балансе {money[team]}')
                    des = int(input('Покупаем? 100 ед. топлива?'
                                    '1 - да, 0 - нет'))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] <= price:
                                food[team] += 500
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
                case 3:
                    price = random.randint(80, 120)
                    print(f'Цена 5000 единиц материала - {price}'
                          f'У вас на балансе {money[team]}')
                    des = int(input('Покупаем? 5000 ед. материала?'
                                    '1 - да, 0 - нет'))
                    match des:
                        case 0:
                            pass
                        case 1:
                            if money[team] <= price:
                                food[team] += 500
                                print('Поздравляем с покупкой!')
                                indicators(team)
                            else:
                                print('У вас недостаточно денег')
        case 0:
            pass


def battle_cheater(team, attack_ships):
    if sum(attack_ships) > sum(ships[team]):
        return False
    return True


def battle(team, opponent):
    global ships, planet_systems, oil
    attacker = team
    defender = opponent

    jet, bomber, corvette = 0, 0, 0
    attack_ships = [1000, 1000, 1000]

    while battle_cheater(team, attack_ships) == False:
        print('Император, в вашем распоряжении:',
              f'{ships[team][0]} истребителей',
              f'{ships[team][1]} бомбардировщиков',
              f'{ships[team][2]} корветов', sep = '\n')

        attack_ships = print('Сколько истребителей, '
                             'бомбардировщиков и корветов вы отправите на захват?\n'
                             'Укажите требуемые значения, каждое в новой строке.')

        while jet==0 and bomber==0 and corvette==0:
            try:
                jet = int(input('Сколько истребителей? '))
                bomber = int(input('Сколько бомбардировщиков? '))
                corvette = int(input('Сколько корветов? '))
            except:
                continue

        attack_ships = [jet, bomber, corvette]

    area = 0
    while area == 0:
        try:
            area = int(input(('Введите размер территории для захвата, '
                              f'не больше чем {planet_systems[opponent]} ')))
            if oil[team] < area*2000:
                print('Император, у нас недостаточно топлива для таких расстояний. ',
                      f'Нехватка составляет {area*2500 - oil[team]}')
                return
            oil[team] -= area*2000
        except:
            continue
    p_area = math.ceil(planet_systems[opponent] / area)

    defend_ships = list(map(lambda x: math.ceil(x/p_area), ships[opponent]))


    j1, b1, c1 = attack_ships[0], attack_ships[1], attack_ships[2]
    j2, b2, c2 = defend_ships[0], defend_ships[1], defend_ships[2]

    j1_u, b1_u, c1_u = j1, b1, c1
    j2_u, b2_u, c2_u = j2, b2, c2
    j1_o, b1_o, c1_o = ships[team][0], ships[team][1], ships[team][2]
    j2_o, b2_o, c2_o = ships[opponent][0], ships[opponent][1], ships[opponent][2]

    n=1
    while abs(j1)+abs(b1)+abs(c1) > 0 and abs(j2)+abs(b2)+abs(c2) > 0:
        print('=================================')

        print(f'{n} раунд.',
              f'Число кораблей команды {teams[attacker]}:',
              f'{j1} истребителей, {b1} бомбардировщиков, {c1} корветов',
              f'Число кораблей команды {teams[defender]}:',
              f'{j2} истребителей, {b2} бомбардировщиков, {c2} корветов',
              f'Атакует команда {teams[attacker]}', sep = '\n')
        
        if j1==0 and b1==0 and j2==0 and b2==0:
            c2 -= c1
        elif j1==0 and c1==0 and b2==0 and c2==0:
            b2 -= b1
        elif b1==0 and c1==0 and b2==0 and c2==0:
            j2 -= j1

        j2 = 0 if (j2 - c1)<0 else (j2 - c1)
        b2 = 0 if (b2 - j1)<0 else (b2 - j1)
        c2 = 0 if (c2 - b1)<0 else (c2 - b1)

        attacker, defender = defender, attacker
        j1, j2 = j2, j1
        b1, b2 = b2, b1
        c1, c2 = c2, c1
        n+=1


    print('=================================')

    if j1+b1+c1 == 0 and n%2!=0:
        print(f'Победила команда {teams[opponent]}')
        ships[team] = [0, 0, 0]
        ships[opponent] = [j2_o - j2_u + j2,
                           b2_o - b2_u + b2,
                           c2_o - c2_u + c2]
    elif j1+b1+c1 == 0 and n%2==0:
        print(f'Победила команда {teams[team]}')
        planet_systems[team] += area
        planet_systems[opponent] -= area
        ships[team] = [j1_o - j1_u,
                       b1_o - b1_u,
                       c1_o - c1_u]
        ships[opponent] = [j2_o - j2_u,
                           b2_o - b2_u,
                           c2_o - c2_u]
    elif j2+b2+c2 == 0 and n%2!=0:
        print(f'Победила команда {teams[team]}')
        planet_systems[team] += area
        planet_systems[opponent] -= area
        ships[team] = [j1_o - j1_u,
                       b1_o - b1_u,
                       c1_o - c1_u]
        ships[opponent] = [j2_o - j2_u,
                           b2_o - b2_u,
                           c2_o - c2_u]
    elif j2+b2+c2 == 0 and n%2==0:
        print(f'Победила команда {teams[opponent]}')
        ships[team] = [0, 0, 0]
        ships[opponent] = [j2_o - j2_u + j1,
                           b2_o - b2_u + b1,
                           c2_o - c2_u + c1]
    
    print(f'Число кораблей команды {teams[team]}',
          f'{ships[team][0]} истребителей',
          f'{ships[team][1]} бомбардировщиков',
          f'{ships[team][2]} корветов', sep = '\n')
    print(f'Число кораблей команды {teams[opponent]}',
          f'{ships[opponent][0]} истребителей',
          f'{ships[opponent][1]} бомбардировщиков',
          f'{ships[opponent][2]} корветов', sep = '\n')


def battle_choose(team):
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
    print(f'Играет команда {teams[team]}!')

    event(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    income(team)

    costs(team)

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')

#    trade(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    battle_choose(team)
    input('Вы хотите продолжить? ')
    print('=================================')

    indicators(team)
    input('Вы хотите продолжить? ')
    print('=================================')


def main():
    global planet_systems, money, population, materials, oil, food, min_stations, teams, count_teams
    start(teams)
    input('Вы хотите продолжить? ')
    print('=================================')

    count_revers = 0
    while check_victory(planet_systems, materials, count_teams) == False:
        for team in teams:
            play(team)
            if check_loss(planet_systems, population) == True:
                count_teams -= 1
                break

        if count_teams == 2 and count_revers == 0:
            count_revers+=1
            teams = dict(reversed(teams.items()))

    
    else:
        if planet_systems[0] >= 80:   print(f'Выиграла команда {teams[0]}!')
        elif planet_systems[1] >= 80: print(f'Выиграла команда {teams[1]}!')
        elif planet_systems[2] >= 80: print(f'Выиграла команда {teams[2]}!')
        elif materials[0] >= 55000:  print(f'Выиграла команда {teams[0]}!')
        elif materials[1] >= 55000:  print(f'Выиграла команда {teams[1]}!')
        elif materials[2] >= 55000:  print(f'Выиграла команда {teams[2]}!')
        elif teams.get(0) != None:  print(f'Выиграла команда {teams[0]}!')
        elif teams.get(1) != None:  print(f'Выиграла команда {teams[1]}!')
        elif teams.get(2) != None:  print(f'Выиграла команда {teams[2]}!')


if __name__ == '__main__':
    main()