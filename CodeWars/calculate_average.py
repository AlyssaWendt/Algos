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
    
    #or
    
def find_average(numbers):
    return 0 if len(numbers) == 0 else sum(numbers) / len(numbers)
    
print(find_average([]))
print(find_average([1,2,3,4]))