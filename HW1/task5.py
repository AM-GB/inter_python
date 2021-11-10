deposit = [
    {
        'begin_sum': 1000,
        'end_sum': 10000,
        '6': 5,
        '12': 6,
        '24': 5,
    },
    {
        'begin_sum': 10000,
        'end_sum': 100000,
        '6': 6,
        '12': 7,
        '24': 6.5,
    },
    {
        'begin_sum': 100000,
        'end_sum': 10000000,
        '6': 7,
        '12': 8,
        '24': 7.5,
    }
]


def bank_deposit(amount, tern, replenishment=0):
    product = {}
    sum = amount
    s = 0  # сумма по процентам

    for d in deposit:
        if d['begin_sum'] <= amount < d['end_sum']:
            product = d
            break
    else:
        return f'Неверная сумма'

    if str(tern) in product.keys():
        for m in range(tern):
            if m == 0 or m == tern - 1:
                s += (sum*product[str(tern)]*(30/365))/100
            else:
                sum += replenishment
                s += (sum*product[str(tern)]*(30/365))/100

    else:
        return f'Неверный срок'

    return f'сумму вклада на конец срока: {(sum + s)}'


if __name__ == '__main__':

    print(bank_deposit(15000, 6, 1000))
