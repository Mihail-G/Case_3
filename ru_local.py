OIL = 'Топливо'
MATERIALS = 'Материалы'
FOOD = 'Еда'
STATIONS_NAME_PROD = 'продовольственных'
STATIONS_NAME_MAT = 'материало-добывающих'
STATIONS_NAME_OIL = 'топливо-добывающих'

START_TEAM_O = 'Введите название первой команды '
START_TEAM_1 = 'Введите название второй команды '
START_TEAM_2 = 'Введите название третьей команды '
START_SCREEN = ('Вы - император космических земель',
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
          '5 истребителей')

def lose(teams, team):
    return f'Команда {teams[team]} проиграла!'

NOT_ENOUGH_PROD = 'Император, у вас нехватка продовольствия в размере'
DIE = 'Погибло'
STOCKS_OUT = 'населения, запасы продовольствия истощены'
NOT_ENOUGH_OIL = 'Император, у вас нехватка топлива для обеспечения исправной работы добывающих станций'
OUT = 'Выведено из строя'
STATIONS_OUT = 'рабочих станций, запасы топлива истощены'
NOT_ENOUGH_POP = 'Император, у вас нехватка населения для обеспечения исправной работы добывающих станций'
STAT = 'рабочих станций'
OVERPOP = 'Император, ваши планеты перенаселены, люди умирают'
POP = 'населения'

def indic_ret(team, planet_systems, population, money, materials, oil, food, min_stations):
    return ('Император, представляем к вашему вниманию последние экономические '
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
          'Вы можете построить еще ')