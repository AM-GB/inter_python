try:
    num = input('Введите число: ').split('.')
    map(lambda x: int(x), num)
    if len(num) == 1 and num[0].isdigit():
        print('Введенное число целое')
        exit(0)
    print(num[0] == num[1])

except Exception as e:
    print(e)
    print('Это не число')
