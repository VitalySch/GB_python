profit = int(input('Введите доход: '))
loss = int(input('Введите издержки: '))
if profit > loss:
    print(f'Ваш доход составляет {profit - loss}')
    workers = int(input('Введите количество сотрудников: '))
    print(f'Средний доход на одного сотрудника {(profit - loss) / workers:.2f}')
elif profit < loss:
    print(f'Ваш убыток составляет {loss - profit}')
else:
    print(f'Вы ничего не заработали.')
git