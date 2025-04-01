def oli_down_ev(oil, team):
    oil[team] //= 2
    print('Ой, произошла утечка!',
          'Ваши запасы топлива сократились в 2 раза')

def oli_down_ev1(oil, team):
    oil[team] //= 1.5
    print('Ой, произошла утечка!',
          'Ваши запасы топлива сократились в 1.5 раза')

def oli_up_ev(oil, team):
    oil[team] *= 2
    print('Химики ударники!',
          'Ваши запасы топлива увеличились в 2 раза')

def oli_up_ev1(oil, team):
    oil[team] *= 1.5
    print('Химики ударники!',
          'Ваши запасы топлива увеличились в 1.5 раза')

def food_up_ev(food, team):
    food[team] *= 2
    print('Пищевая революция!',
          'Ваши запасы еды увеличились в 2 раза')

def food_up_ev1(food, team):
    food[team] *= 1.5
    print('Пищевая революция!',
          'Ваши запасы еды увеличились в 1.5 раза')

def food_down_ev(food, team):
    food[team] //= 2
    print('Гидропоника дала сбой!',
          'Ваши запасы еды уменьшились в 2 раза')

def food_down_ev1(food, team):
    food[team] //= 1.5
    print('Гидропоника дала сбой!',
          'Ваши запасы еды уменьшились в 1.5 раза')

def population_up_ev(population, team):
    population[team] *= 1.5
    print('Бейбибум!',
          'Население увеличилось в 1.5 раза')

def population_up_ev1(population, team):
    population[team] *= 1.1
    print('Сезон рождаемости!',
          'Население увеличилось на 10%')

def population_down_ev(population, team):
    population[team] //= 2
    print('Массовое вымирание',
          'Население уменьшилось в 2 раза')

def population_down_ev1(population, team):
    population[team] //= 1.1
    print('Демографическая яма',
          'Население уменьшилось на 10%')

def money_up_ev(money, team):
    money[team] += 100
    print('Межгалактическое правительство расщедрилось',
          'На ваш денежный счет начислялись 100 д.е.')

def money_up_ev1(money, team):
    money[team] += 1000
    print('Межгалактическое правительство раздает резервы',
          'На ваш денежный счет начислялись 1000 д.е.')

def money_up_ev2(money, team):
    money[team] += 5000
    print('На Вашу планетарную систему упал корабль с деньгами',
          'На ваш денежный счет начислялись 5000 д.е.')

def money_down_ev(money, team):
    money[team] //= 2
    print('Всем подданным налоговый вычет!',
          'Ваш денежный счет уменьшился в 2 раза')

def money_down_ev1(money, team):
    money[team] //= 3
    print('Галопирующая звезда разрушила несколько планет в звездной системе!',
          'Ваш денежный счет уменьшился в 3 раза')

def money_down_ev2(money, team):
    money[team] //= 4
    print('Межзвездное ДТП! Планеты столкнулись',
          'Ваш денежный счет уменьшился в 4 раза из-за реконструкций')

def planet_systems_up_ev (planet_systems, team):
    planet_systems[team] += 5
    print('Ваши ученые сделали прорыв в исследовании космоса!',
          'Ваши владения увеличились на 5 планетных систем')

def planet_systems_up_ev1 (planet_systems, team):
    planet_systems[team] += 10
    print('Туманность развеялась',
          'Ваши владения увеличились на 10 планетных систем')

def planet_systems_up_ev2 (planet_systems, team):
    planet_systems[team] += 15
    print('Ранее неизведанная малая империя присоединилась к Вам',
          'Ваши владения увеличились на 15 планетных систем')

def planet_systems_down_ev (planet_systems, team):
    planet_systems[team] -= 5
    print('Апокалипсис наяву!',
          'Ваши владения уменьшились на 5 планетных систем')

def planet_systems_down_ev1 (planet_systems, team):
    planet_systems[team] -= 10
    print('Метеоры решили порешить Вас!',
          'Ваши владения уменьшились на 10 планетных систем')

def planet_systems_down_ev2 (planet_systems, team):
    planet_systems[team] -= 15
    print('Пупупу, ну, желаем удачи...',
          'Ваши владения уменьшились на 15 планетных систем')

def planet_systems_down_ev3 (planet_systems, team):
    planet_systems[team] //= 2
    print('Черная дыра-изгой прямо по курсу! Все как и завещал Стивен Хокинг...',
          'Количество ваших планетарных систем уменьшилось в 2 раза')

def materials_down_ev (materials, team):
    materials[team] //= 2
    print('Производственный брак',
          'Материалы уменьшились в 2 раза')

def materials_down_ev1 (materials, team):
    materials[team] -= 100
    print('Вор на производстве',
          'Материалы уменьшились на 100 единиц')

def materials_down_ev2 (materials, team):
    materials[team] //= 5
    print('Шабат',
          'Материалы уменьшились в 5 раз')

def materials_up_ev (materials, team):
    materials[team] *= 2
    print('Сверх плана"',
          'Материалы увеличились в 2 раза')

def materials_up_ev1 (materials, team):
    materials[team] += 250
    print('Кто сказал что детский труд это плохо?',
          'Материалы увеличились на 250 ед')

def materials_up_ev2 (materials, team):
    materials[team] *= 2
    print('Автора новостей отправили на завод',
          'материалы увеличились в 2 раза')

def mat_station_up_ev (min_stations, team):
    min_stations[team][1] *= 1.5
    print('Взрыв машиностроения!',
          'Количество материало-добывающих станций увеличилось в 1.5 раза')

def mat_station_down_ev (min_stations, team):
    min_stations[team][1] //= 2
    print('Отказ оборудования!',
          'Количество материало-добывающих станций уменьшилось в 2 раза')

def prod_station_up_ev (min_stations, team):
    min_stations[team][0] *= 2
    print('Бум сельскохозяйственной промышленности',
          'Количество продовольство-добывающих станций увеличилось в 2 раза')

def prod_station_down_ev (min_stations, team):
    min_stations[team][0] //= 2
    print('Упадок сельскохозяйственной промышленности',
          'Количество продовольство-добывающих станций уменьшилось в 2 раза')

def oil_station_up_ev (min_stations, team):
    min_stations[team][2] *= 2
    print('Прибыль Национального достояния делает Stongs!',
          'Количество топливо-добывающих станций увеличилось в 2 раза')

def oil_station_down_ev (min_stations, team):
    min_stations[team][2] //= 2
    print('Прибыль Национального достояния делает вниз',
          'Количество топливо-добывающих станций уменьшилось в 2 раза')