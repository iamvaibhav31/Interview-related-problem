"""
Give an array of integers (positive and negative) find the largest continuous sum ?

"""
# ----------------------------------------------------- #
# ___METHORD 1___ #

def large_cout_sum(arr):
    if len(arr)==0:
        return 0
    
    current_sum = arr[0]
    max_sum  = arr[0]
    
    for num in arr[1:]:
        current_sum = max(current_sum + num , num)
        max_sum = max(current_sum , max_sum)

    return max_sum

# ___END___ # 
# ----------------------------------------------------- #
print(large_cout_sum([1,2,-1,3,4,10,10,-10,-1]))
