# Задача №1
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары:')
    for b, g in tuple(zip(sorted(boys), sorted(girls))):
        print(f'{b} и {g}')
else:
    print('Количество людей в списках не совпадает, знакомить не будем, т.к. кто-то может остаться без пары!')

# Задача №2
cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]

person = 5
s = ''
st = ''

for el in range(len(cook_book)):
    for i in range(len(cook_book[el][1])):
        cook_book[el][1][i][1] *= person

for el_cook_book in cook_book:
    print(f'{(el_cook_book[0]).capitalize()}:')
    for ingredient in el_cook_book[1]:
        s = ''.join([str(ingredient[1]), ingredient[2]])
        ingredient[1] = s
        ingredient = ingredient[:2]
        st = ', '.join(ingredient)
        print(st)
    print()
