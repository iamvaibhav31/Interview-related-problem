"""
consider  an array of non- negative. A second array is formed 
by shuffling the elements of the first array and deleting a 
random element. Given these two arrays find which element is 
missing in the second array.

Here is an example input , the first is shuffled and the 
number 5 in removed to  construct the second array 

Input:
    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
    The missing element is := 5
"""
# ------------------------------------------------- #

import collections

# ------------------------------------------------- #
# ___ METHORD 1 ___ #

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1!=num2:
            return num1

    return arr1[-1]

# ___ END ___ #
# ------------------------------------------------- #
# ___ METHOR 2 ___ #

def finder1(arr1 , arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
            
# ___END___ #
# ------------------------------------------------#'
if __name__="__main__":
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [3,7,2,1,4,6] 
    print("The missing element is :- ",finder(arr1,arr2))
    print("The missing element is :- ",finder1(arr1,arr2))
