a = int(input('Введите количество секунд: '))
hours = a // 3600
minutes = a % 3600 // 60
seconds = a % 3600 % 60
print(f'{hours}:{minutes}:{seconds}')