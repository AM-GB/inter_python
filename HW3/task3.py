from random import randint

lst_key = [f'k{n}' for n in range(randint(1, 10))]
lst_value = [f'v{n}' for n in range(randint(1, 10))]

dir_lst = {}

j = len(lst_value)
for i in range(len(lst_key)):
    if i < j:
        dir_lst[lst_key[i]] = lst_value[i]
        continue
    dir_lst[lst_key[i]] = None

print(lst_key, '\n', lst_value, '\n', dir_lst)
