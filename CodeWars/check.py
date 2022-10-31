def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False      
        
print(check([101, 45, 75, 105, 99, 107], 107))