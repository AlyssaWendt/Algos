'''
Create a function that takes an integer as an argument and returns
"Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    if number == 0:
        print("Zero")
    elif number % 2 != 0:
        print("Odd")
    else:
        print("Even")
        
even_or_odd(8)
even_or_odd(1)