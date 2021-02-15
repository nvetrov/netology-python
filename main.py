# Задача №2
if __name__ == '__main__':
    sd = float(input('Введите длину стороны квадрата: '))
    print('Вывод:')
    print('Периметр:', 4 * sd)
    print('Площадь:', sd ** 2)

    length_rectangle = float(input('Введите длину прямоугольника:'))
    width_rectangle = float(input('Введите ширину прямоугольника:'))
    perimeter = length_rectangle * 2 + width_rectangle * 2
    area = length_rectangle * width_rectangle

    print('Вывод:')
    print("Периметр: %.2f " % perimeter)
    print("Площадь: %.2f " % area)
# Задача №3
income = float(input('Введите заработную плату в месяц:'))
percent = float(input('Введите, какой процент(%) уходит на ипотеку:'))
percent_for_live = float(input('Введите, какой процент(%) уходит на жизнь:'))
print('Вывод:')

percent_years = ((percent / 100) * income) * 12
accumulate = 100 - (percent + percent_for_live)
accumulate_years = ((accumulate / 100) * income) * 12

print(f'На ипотеку было потрачено: {percent_years} рублей')
print(f'Было накоплено: {accumulate_years} рублей')
