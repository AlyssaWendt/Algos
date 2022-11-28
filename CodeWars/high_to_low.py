def high_and_low(numbers):
    num = sorted(numbers.split(), key=int)
    return f"{num[-1]} {num[0]}"

print(high_and_low("1 2 3"))
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))