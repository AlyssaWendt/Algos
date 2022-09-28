''' 
-----------------------------------------------------------------

Prompt:
- Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
- A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.

Examples:

is_prime(2) //=> true
is_prime(3) //=> true 
is_prime(4) //=> false
is_prime(29) //=> true
is_prime(200) //=> false

-----------------------------------------------------------------*/
'''
#0 and 1 are never prime, so should always return False.

#The number 2 should return True, 
#but won't fit conveniently in the range() function, 
#as described by other commenters.

def is_prime(x):             
    if x == 0 or x == 1:
        return False
    elif x == 2:
        return True
    for n in range(2,x-1):   
        if x % n == 0:       
            return False
    else:                    
        return True


print(is_prime(200))