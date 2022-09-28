'''
*******************************************************************************
Write a function phrase_finder(words, phrase), that takes in an list of words and a
string representing a phrase. The function should return True if the phrase can be
formed by a pair of words from the list. The function should return false if the
phrase cannot be formed by any pair of words.

Examples:

phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye') => False
*******************************************************************************/
'''


def phrase_finder(words, phrase):
    phrase_split= phrase.split(' ')
    for word in phrase_split:
        if word in words:
            print(True)
        else:
            print(False)
            
phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep')
#phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') 
#phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world')
#phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') 
#phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye')

