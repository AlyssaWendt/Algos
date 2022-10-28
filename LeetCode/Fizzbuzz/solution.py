#You write a function that will count from 1-99 printing 1 of four things 
# for each number.
# If the number is divisible by 3, print "fizz".
# If the number is divisible by 5, print "buzz".
# If the number is divisible by 3 and 5, print "fizzbuzz".

def Fizzbuzz(n):
    res = []
    for x in range(1, n):
        if x % 3 ==0  and x % 5 == 0:
            res.append("fizzbuzz") 
        elif x % 5== 0:
            res.append("buzz")
        elif x % 3==0:
            res.append("fizz")
        else:
            res.append(str(x))
        
    return res

print(Fizzbuzz(15))
       
#things to note
# What order the if else statement in is matters
# it will read the intsructions top to bottom 