'''
-----------------------------------------------------------------


Prompt:

- Write a function named prime_factors that accepts a whole number greater 
than one (1) as an argument and returns an list of that argument's prime factors.

- The prime factors of a whole number are the prime numbers that,
when multiplied together, equals the whole number.

- If the argument provided is not greater than 1, or not a whole number, 
then primeFactors should return an empty list.

Examples:

prime_factors(2) //=> [2]
prime_factors(3) //=> [3]
prime_factors(4) //=> [2, 2]
prime_factors(18) //=> [2, 3, 3]
prime_factors(29) //=> [29]
prime_factors(105) //=> [3, 5, 7]
prime_factors(200) //=> [2, 2, 2, 5, 5]

-----------------------------------------------------------------
'''




def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print(factors) 
    
    
prime_factors(4)
prime_factors(200)