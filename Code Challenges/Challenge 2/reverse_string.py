'''
******************************************************************************
Write a function reverse_string(string) that takes in a hyphenated string and
returns a the hyphenated string reversed.

Examples:
reverseString('Go-to-the-store') => 'store-the-to-Go'
reverseString('Jump-jump-for-joy') => 'joy-for-jump-Jump,'
******************************************************************************
'''

def reverseString(s):
    s = s.split("-")
    rev_s ="-".join(s[::-1])
    print(rev_s)

    
reverseString('Go-to-the-store')
reverseString('Jump-jump-for-joy')
    
