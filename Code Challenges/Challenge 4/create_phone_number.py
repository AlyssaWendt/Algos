'''
## 1. **Create Phone Number**

Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

Ex.
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

'''
# change the list of integers into a list of strings
#This will take the index and place them into a format of a phone number

def create_phone_number(list):
    phone = [str(num) for num in list]
    phone_nums = f'({phone[0]}{phone[1]}{phone[2]}) {phone[3]}{phone[4]}{phone[5]}-{phone[6]}{phone[7]}{phone[8]}{phone[9]}'
    print(phone_nums)
    
    
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

