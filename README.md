# Interview-related-problem
There are some interview related problem in python  so lets check out some question :-

# ANAGREM

Q1. write a boolean function that will take two strings and return whether they are anagrams ?


NOTE:- 

ANAGREAM :- A good example problem for showing algorithms with different orders of magnitude is the classic anagram detection problem for strings. One string is an anagram of another if the second is simply a rearrangement of the first. For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. For the sake of simplicity, we will assume that the two strings in question are of equal length and that they are made up of symbols from the set of 26 lowercase alphabetic characters. 

Input:
    
    public relation  crap built on lies
    
 Output:
 
    True
# ARRAY FIND MISSING ELEMENT

Q2. consider  an array of non-negative. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays find which element is missing in the second array.

Here is an example input , the first is shuffled and the number 5 in removed to  construct the second array ?

Input:

    [1,2,3,4,5,6,7] [3,7,2,1,4,6]

Output:

    The missing element is := 5

# LARGEST CONTINUOUS SUM IN ARRAY

Q3. Give an array of integers (positive and negative) find the largest continuous sum ?

Input:

    1,2,-1,3,4,10,10,-10,-1
    
Output:

    29

# ARRAY PAIR SUM 

Q4. Given an integer array , output all the unique pair that sum up to a specific value K ?

Input:
    
    [1,3,2,2] 4
    
Output:

    (1,3)
    (2,2)

# STRING COMPRESSION 

Q5. Given a string in the form 'AAABBBAACCEE' compress it to become 'A3B3A2C2E2' .For this problem you can falsely "compress" strings of single or duble letters . For instnce ,it is okay for 'AAB' of return 'A2B1' even though this tehiinically take ore space.

The function should also be a case sensitive 'AAAaaa' retuns 'A3a3'

Input 1 :

    AAABCEEE
    
Output :

    A3B1C1E3
    
Input 2 :

    AAAaaa
    
Output :

    A3a3

# UNIQUE CHARACTER STRING 

Q6. Given a string , determine if it is compreised of all the unique character .for example the string 'abcde' has all  unique characters and should return True. The string 
'aabbss' contain dublicate character and shaould retune false.

Input:

    abcd
    
Output:

    True
    
# IMPLEMENT A QUEUE - USING TWO STACK

Q7. Gven the stack class below implement a queue class using two stacks 
