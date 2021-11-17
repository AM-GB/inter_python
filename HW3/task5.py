from random import randint


def file_handler(file):
    with open(file, 'tw', encoding='utf-8') as f:
        print(file + '\n')

    lst1 = [randint(1, 20) for _ in range(randint(1, 20))]
    lst2 = [f'str{n}' for n in range(randint(1, 20))]

    lst = list(zip(lst1, lst2))

    with open(file, 'w') as f:
        for i in lst:
            f.write(f'{i[0]}  {i[1]}\n')

    print_file(file)


def print_file(file):
    with open(file) as f:
        lst = f.read()

    lst = lst.replace('1', 'rep')

    with open(file, 'w') as f:
        f.write(lst)

    with open(file) as f:
        for line in f:
            print(line)


if __name__ == '__main__':
    file_handler('1.txt')
