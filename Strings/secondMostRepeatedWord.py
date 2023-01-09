#############################
# Second Most Repeated Word #
#############################

'''
Given a sequence of strings, the task is to find out the 
second most repeated (or frequent) string in the given sequence.
'''

def second_repeat(arr, n):
    occ = {}
    for i in range(len(arr)):
        occ[arr[i]] = occ.get(arr[i], 0) + 1
    
    first_max = -10**8
    sec_max = -10**8
    
    for it in occ:
        if (occ[it] > first_max):
            sec_max = first_max
            first_max = occ[it]
                
        elif (occ[it] > sec_max and occ[it] != first_max):
            sec_max = occ[it]
        
    for it in occ:
        if (occ[it] == sec_max):
            return it
            
    return ""


def main():
    n = int(input())
    arr = input().strip().split()
    print(second_repeat(arr, n))
       

if __name__ == "__main__":
    main()


'''
Example 1:
Input:
N = 6
arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
Output: bbb
Explanation: "bbb" is the second most occurring string with frequency 2.


Example 2:
Input: 
N = 6
arr[] = {geek, for, geek, for, geek, aaa}
Output: for
Explanation: "for" is the second most occurring string with frequency 2.
'''