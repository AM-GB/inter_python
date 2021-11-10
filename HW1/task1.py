def multiplication_table(a, b):
    lst, row = [], []
    num, mult = 1, 0
    for i in range(1, b+1):
        for j in range(a):
            mult += 1
            row.append(num*mult)
            if mult == 10:
                mult = 0
                num += 1
        lst.append(row[:])
        row.clear()
    return lst


if __name__ == '__main__':
    l = list(map(lambda n: str(n), multiplication_table(5, 5)))

    print(type(l[0][0]))

    for i in l:
        print(i)
