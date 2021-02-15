# TODO Я работаю секретарем и мне постоянно приходят различные документы.
#  Я должен быть очень внимателен чтобы не потерять ни один документ.
#  Каталог документов хранится в следующем виде:
from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

'''

Задача №1
Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
 когда пользователь будет пытаться добавить документ на несуществующую полку.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.
'''


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def people_doc(lst, num):
    for n in lst:
        if num == (n['number']):
            print(n['name'])
            break
    else:
        print(f'Номер документа "{num}" не найден.')


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf_doc(dct, s):
    for key in dct:
        if s in dct[key]:
            print(key)
            break
    else:
        print(f'Номер документа "{s}" не найден.')


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_doc(lst):
    for d in lst:
        print(d["type"], f'"{d["number"]}" "{d["name"]}";')


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
def add_doc(add_l, doc, dct):
    new_doc = dict()
    new_doc['type'] = add_l[1]
    new_doc['number'] = add_l[0]
    new_doc['name'] = add_l[2]
    doc.append(new_doc)
    if add_l[3] not in dct.keys():
        print(f'{add_l[3]} полки не существует')
    else:
        dct[add_l[3]].append(add_l[0])
        # print(dct)
    return True


'''
Задача №2. Дополнительная (Обязательная)
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
'''


# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
# Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
def delete_doc(lst, dct, num_doc):
    for element in lst:
        for key, value in element.items():
            if value == num_doc:
                element[key] = None
                pprint(lst)
                break
    # pprint(lst)
    for key in dct:
        if num_doc in dct[key]:
            dct[key].remove(num_doc)
            # print(dct)
            # print()
            print(f'"{num_doc}" удалён!')
            break
    else:
        print(f'"{num_doc}" несуществующий докумен!')


# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ
# или переместить документ на несуществующую полку;
def move_doc(dct, num_doc_current):
    num_d_value, move_key_pos = num_doc_current

    doc_value = False
    doc_shelf = False

    # Полка существует?
    for key in dct.keys():
        if move_key_pos == key:
            doc_shelf = True
            # print(f'"doc_shelf", {move_key_pos}, {doc_shelf}')
            break

    # Документ сужествует?
    for value in dct.values():
        if num_d_value in value:
            doc_value = True
            # print(f'"doc_value", {num_d_value}, {doc_value}')
            break

    if doc_value is False:
        print(f'Пытаетесь переместить несуществующий документ "{num_d_value}";')
    if doc_shelf is False:
        print(f'Полка "{move_key_pos}" не существует;')
    if (doc_shelf is True) and (doc_value is True):
        # add
        for key, value in dct.items():
            if move_key_pos in key:
                dct[key].append(num_d_value)
                break
        # def
        for key, value in dct.items():
            if num_d_value in value:
                dct[key].remove(num_d_value)
                break
    # print(dct)


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
# Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

def add_shelf(dct, shelf_num):
    for key in dct:
        if shelf_num == key:
            print('Полка уже существует.')
    dct.setdefault(shelf_num, [])
    # print(dct)


def main():
    answer = False

    while answer is not True:
        input_data = input('Введите команду: ')

        if input_data == 'p':
            people = input('Введите номер документа: ')
            people_doc(documents, people)
        elif input_data == 's':
            shelf = input('Введите номер документа: ')
            shelf_doc(directories, shelf)
        elif input_data == 'l':
            list_doc(documents)
        elif input_data == 'a':
            try:
                add_lst = (input(
                    'Введите номер документа, тип, имя владельца и номер полки через запятую(без пробела): ')).split(
                    ',')
                # add_lst = ['666', 'тип', 'имя владельца', '5'] #-->  666,тип,имя владельца,2
                add_doc(add_lst, documents, directories)
            except IndexError:
                add_lst = (input(
                    'Введите  номер документа, тип, имя владельца и номер полки через запятую(без пробела):: ')).split(
                    ',')
                add_doc(add_lst, documents, directories)
        elif input_data == 'd':
            num_doc = input('Введите номер документа: ')
            delete_doc(documents, directories, num_doc)

        elif input_data == 'm':
            num_doc_d = input('Введите номер документа и целевую полку через запятую(без пробела): ').split(',')
            move_doc(directories, num_doc_d)

        elif input_data == 'as':
            shelf_num = input('Введите номер новой полки:')
            add_shelf(directories, shelf_num)

        else:
            print('Внимание: p, s, l, a, d, m, as - это пользовательские команды')
            answer = True


# Start here:
main()
