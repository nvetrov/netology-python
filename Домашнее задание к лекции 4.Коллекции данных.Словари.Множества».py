# #  TODO: Задание 1. Дан список с визитами по городам и странам.
# #   Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России.
from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

russian_geo_logs = []

for log in range(len(geo_logs)):
    for key, item in geo_logs[log].items():
        if 'Россия' in item[1]:
            russian_geo_logs.append(geo_logs[log])
pprint(russian_geo_logs)

# TODO Задание 2. Выведите на экран все уникальные гео-ID из значений словаря ids.
#  Т. е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_values = []

for unique in ids:
    unique_values.extend(ids[unique])
print(list(set(unique_values)))

# TODO: Задание 3. Дан список поисковых запросов. Получить распределение количества слов в них.
#  Т. е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

queries_total = len(queries)
dct_words = dict()

for q in range(len(queries)):
    dct_words.setdefault(len(queries[q].split(' ')), 0)
    dct_words[len(queries[q].split(' '))] += 1

print('Поисковых запросов из: ')
for key in dct_words:
    dct_words[key] = round((100 * dct_words[key]) / queries_total)
    print(f'{key} слов - {dct_words[key]}%')

#  TODO Задание 4. Дана статистика рекламных каналов по объемам продаж.
#   Напишите скрипт, который возвращает название канала с максимальным объемом.
#   Т. е. в данном примере скрипт должен возвращать 'yandex'.

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

print(*[key for key, value in stats.items() if value == max(stats.values())])

# TODO: Задание 5. *(Необязательное) Напишите код для преобразования произвольного списка вида
#  ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

lst_originals = ['2018-01-01', 'yandex', 'cpc', 100]


def function(list_of_elem):
    d_total = dict()
    while len(list_of_elem) >= 2:
        for element in range(len(list_of_elem)):
            if element == len(list_of_elem) - 1:
                d_total.setdefault(list_of_elem[-2], list_of_elem[-1])
                del list_of_elem[-1]
                list_of_elem[-1] = d_total
                function(list_of_elem)
            else:
                continue
    return list_of_elem


print(*function(lst_originals))
