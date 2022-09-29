'''
******************************************************************************
Write a function intersect(list1, list2) that takes in two lists and returns a
new list containing the elements common to both list1 and list2.

Hint: use index()

Examples:

intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']) => [ 'b', 'd' ]
intersect(['a', 'b', 'c'], ['x', 'y', 'z']) => []
*******************************************************************************/
'''

def intersect(list1,list2):
    new_list = []
    for a in list1:
        if a in list2:
            new_list.append(a)
    print(new_list)
          
            
            
intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']) 
            
            

     
     

     