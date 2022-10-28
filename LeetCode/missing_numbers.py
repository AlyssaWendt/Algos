def missingNumber(nums):
    nums.sort(reverse=True)
    list = []
    result = []
    #print(nums)
    for i in range(nums[0]):
        list.append(i)
    for j in range(len(list)):
        if list[j] not in nums:
            return list[j]
    
       
            
def mN(nums):
    len_n = len(nums)
    res = len_n
 
    for i in range(len_n):
        res ^= i ^ nums[i] 
        # In Python, XOR is a bitwise operator that is also known as Exclusive OR.
        #  The symbol for XOR in Python is '^' and in mathematics, its symbol is '⊕'.
    return res
             
        
        

print(mN([0,1]))       
            
            
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))