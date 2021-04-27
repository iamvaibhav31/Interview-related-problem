"""
Given a string in the form 'AAABBBAACCEE' compress it to become 'A3B3A2C2E2' .For this problem you can falsely "compress" 
strings of single or duble letters . For instnce ,it is okay for 'AAB' of return 'A2B1' even though this tehiinically take ore 
space.

The function should also be a case sensitive 'AAAaaa' retuns 'A3a3'
"""

# METHORD_1 

def compress(s):

    r = ""
    l = len(s)
     #BEST_CASE
    if l == 0:
        return ""
     #AVERAGE_CASE
    if l == 1:
        return s+"1"
    #WORST_CASE
    last = s[-1]
    cnt = 1
    i = 1

    while i < l:

        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
      
        i += 1

    r = r + last + str(cnt)
    
    return r

# METHORD_2

def compress1(word):
    #BEST_CASE
    if len(word) == 0:
        return ""
    #AVERAGE_CASE
    if lle(word) == 1:
        return word+"1"
    #WORST_CASE
    layer = []
    for i in word:
        if i not in layer:
            count=word.count(i)
            layer+= i+str(count)
    result = "".join(layer)
    return result

print(compress("AAaabbCcB"))
print(compress("vaibhav"))
print(compress1("AAaabbCcB"))
print(compress1("vaibhav"))
