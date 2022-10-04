# [1, -3, -4, 8, 2] => 7
# [2, -3] => 2

def monkey_jump(jumps):
    total = 0
    lowest = 0
    for jump in jumps:
        total += jump
        if total < lowest:
            lowest = total
    return 1 - lowest

print(monkey_jump([1, -3,-4,8,2]))
print(monkey_jump([2,-3]))
    