def decimal_translator_2(n, base):
    nums = '0123456789abcdefghijklmnopqrstuvwxyz'
    summa = 0
    for i in range(len(n)):
        if nums.find(n[i].lower()) >= base:
            return('None')
        else:
            summa += nums.find(n[i].lower()) * base**(len(n) - 1 - i)
    return summa