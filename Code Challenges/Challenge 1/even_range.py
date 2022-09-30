'''
*******************************************************************************
Write a function even_range(start, end) that returns an list containing all even
numbers between 'start' and 'end' in sequential order.
Examples:
even_range(13, 20) => [ 14, 16, 18, 20 ]
even_range(4, 11) => [ 4, 6, 8, 10 ]
even_range(8, 5) => []
*******************************************************************************/
'''

def even_range(a, b):
    li = []
    for i in range(a,b+1):
        if i%2!=0:
            pass
        else:
            li.append(i)
            print(li)
        
#even_range(13,20)
#even_range(4, 11)
#even_range(8, 5)

