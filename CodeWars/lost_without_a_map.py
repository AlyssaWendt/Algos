'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

def maps(a):
    res = []
    for i in a:
        b = i * 2
        res.append(b)
    return res
        
    
print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))