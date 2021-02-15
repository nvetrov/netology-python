directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

num_doc_d = ['10006', '3']

num_d_value, move_key_pos = num_doc_d

doc_value = False
doc_shelf = False

# Полка существует?
for key in directories.keys():
    if move_key_pos == key:
        doc_shelf = True
        print(f'"doc_shelf", {move_key_pos}, {doc_shelf}')
        break

# Документ сужествует?
for value in directories.values():
    if num_d_value in value:
        doc_value = True
        print(f'"doc_value", {num_d_value}, {doc_value}')
        break

if doc_value is False:
    print(f'Пытаетесь переместить несуществующий документ "{num_d_value}";')
if doc_shelf is False:
    print(f'Полка "{move_key_pos}" несуществует;')
if (doc_shelf is True) and (doc_value is True):
    # add
    for key, value in directories.items():
        if move_key_pos in key:
            directories[key].append(num_d_value)
            break
    # def
    for key, value in directories.items():
        if num_d_value in value:
            directories[key].remove(num_d_value)
            break
print(directories)
