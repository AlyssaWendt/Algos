'''
Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not capitalized 
in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

(Solution)
Split the given string, using the string split() method, which 
returns the list of words present in the string.

Capitalize every word in the list using capitalize method().

And at last, concatenate the words using the join method.
'''

def to_jaden_case(string):
    j = ' '.join([word.capitalize() for word in string.split()])
    return j
    
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))