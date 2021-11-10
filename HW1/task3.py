import random


def random_number_generator(num1, num2):
    dir_el = {}
    amount_el = random.randint(1, 30)

    lst_rand = [random.randint(num1, num2) for n in range(amount_el)]
    lst_rand = list(filter(lambda num: num != 0, lst_rand))

    for i in enumerate(lst_rand):
        key = f'elem_{(i[0]+1)}'
        dir_el[key] = i[1]

    return lst_rand, dir_el


if __name__ == '__main__':
    print(random_number_generator(-10, 100))
