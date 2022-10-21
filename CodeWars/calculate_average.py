'''
Write a function which calculates the average of the numbers 
in a given list.

Note: Empty arrays should return 0.
'''


def find_average(numbers):
    if(numbers == []):
        return 0
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    average = sum / len(numbers)
    return average
    
    
print(find_average([]))
print(find_average([1,2,3,4]))