"""
Given a string , determine if it is compreised of all the
unique character .for example the string 'abcde' has all 
unique characters and should return True. The string 
'aabbss' contain dublicate character and shaould retune 
false
"""

def uni_char(s):
    return len(set(s)) == len(s)

def uni_char1(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    
    return True

print(uni_char("aarriivm"))
print(uni_char1('abcde'))
     