def ten_to_n(num, base):
    answer = str()
    if base < 10:
        while num > 0:
            answer = str(num % base) + answer
            num //= base
    else:
        while num > 0:
            answer = chr(num % base + 64) + answer
            num //= base
print(ten_to_n(255, 2))