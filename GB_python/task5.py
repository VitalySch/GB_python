profit = int(input('Введите доход: '))
loss = int(input('Введите издержки: '))
if profit > loss:
    print(f'Ваш доход составляет {profit - loss}')
    workers = int(input('Введите количество сотрудников: '))
    print(f'Средний доход на одного сотрудника {(profit - loss) / workers:.2f}')
else:
    print(f'Ваш убыток составляет {loss - profit}')
