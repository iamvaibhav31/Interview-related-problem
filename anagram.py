"""
A good example problem for showing algorithms with different orders of magnitude is the classic anagram detection problem for strings. One string is an anagram of another 
if the second is simply a rearrangement of the first. For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. For the sake of 
simplicity, we will assume that the two strings in question are of equal length and that they are made up of symbols from the set of 26 lowercase alphabetic characters. 
Our goal is to write a boolean function that will take two strings and return whether they are anagrams.
"""

def anagram(s1 , s2): # methord 1
    s1 = s1.replace(' ','').lower()
    s2 = s1.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

def anagram2(s1 , s2): # methord 2
    s1 = s1.replace(' ','').lower()
    s2 = s1.replace(' ','').lower()

    if len(s1) != len(s2):
        return False
    
    count = {}

    for  letter in s1:
        if letter in count:
           count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2: 
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
        
    for k in count:
        if count[k] != 0:
            return False
        
    return True


print(anagram('public relation','crap built on lies'))
print(anagram2('clint eastwood','old west action'))
