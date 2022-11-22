start_distance = float(input('Сколько километров Вы пробежали в первый день? '))
end_distance = float(input('Сколько километров Вы хотите пробежать? '))
day_distanse = start_distance
day = 1
while day_distanse < end_distance:
    day_distanse += day_distanse * 0.1
    day += 1
print(f'На {day} день вы пробежите не менее {end_distance}.')