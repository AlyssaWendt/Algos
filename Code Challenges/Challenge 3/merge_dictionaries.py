'''
-----------------------------------------------------------------

Prompt:

- Write a function named merge_dictionaries that 
accepts at least two dictionaries as arguments,
merges the properties of the second through n dictionaries into the first object,
then finally returns the first dictionary.

- If any dictionaries have the same property key, values from the object(s) l
ater in the arguments list should overwrite earlier values.

Examples:

merge_dictionaries({}, {'a': 1});  //=> {'a': 1} (same object as first arg)
merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4});  //=> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}, {'b': 22, 'd': 44});  //=> {'a': 1, 'b': 22, 'c': 3, 'd': 44}
-----------------------------------------------------------------
'''


def merge_dictionaries(dict1, *other_dicts):
    for dict in other_dicts:
        dict1.update(dict)
    print(dict1)
    
    
merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4});