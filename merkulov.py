def transfer_from_n_to_10(num, n):
    if n <= 10 or n >= 36:
        return 'Ошибка'
    else:
        return int(num, n)