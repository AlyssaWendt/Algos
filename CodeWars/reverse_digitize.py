def digitize(n):
    res = [int(x) for x in str(n)]
    str(res)
    res.reverse()
    return res
    

print(digitize(35231))