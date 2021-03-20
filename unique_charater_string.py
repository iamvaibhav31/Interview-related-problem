"""
Given a string , determine if it is compreised of all the unique character .for example the string 'abcde' has all unique characters and should return True. The string 'aabbss' 
contain dublicate character and shaould retune false
"""
# ___ METHORD 1 ___ #  
# In this methor we use python inbuild function to solve this problem 
def uni_char(s):
    return len(set(s)) == len(s)
# THIS METHORD TAKING LESS MEMORY ADDRESS OR LESS EXECUTION TIME 
# ___ END ___ #

# ____ METHORD 2 ____ #
# In this methord we are using manul methord to solved this solution 
def uni_char1(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    
    return True
# BUT THIS TAKE LARGE AMOUNT OF MEMORY SPACE OR EXECUTION TIME 
# ___ END ___ # 

# ___ START ___ #
if __name__ == "__main__":
    print(uni_char("aarriivm"))
    print(uni_char1('abcde'))
     
