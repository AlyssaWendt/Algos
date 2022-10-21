'''
There was a test in your class and you passed it.Congratulations!
But you're an ambitious person. You want to know 
if you're better than the average student in your class.

You receive an array with your peers' test scores. 
Now calculate the average and compare your score!

Return True if you're better, else False! 
'''

def better_than_average(class_points, your_points):
    sum = 0
    for i in range(len(class_points)):
        sum += class_points[i]
    average = sum / len(class_points)
    if(your_points > average):
        return True
    else:
        return False
    
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69))