"""

Given an integer array , output all the unique pair that 
sum up to a specific value K
So the input:
    Pair_sum([1,3,2,2],4)

would be return 2 pair :
    (1,3)
    (2,2)

"""
# In this function The big O notation is :- o(n)
def pair_sum(arr,l):
    
    if len(arr)<2:
        return
    
    seen = set()
    output = set()

    for num in arr:
        target = l-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target)),(max(num,target))

    print("\n".join(map(str,list(output))))


                
if __name__="__main__":
    pair_sum([1,3,2,2],4)