#####################################
# Cyclically rotate an array by one #
#####################################

'''
Given an array, rotate the array by one position in clock-wise direction.
'''

def rotate(arr, n):
    # # Approach 1
    # arr.insert(0, arr[-1])
    # arr.pop()
    
    # Approach 2
    j = n
    for i in range(n):
        a = arr[i]
        arr[i] = arr[j-1]
        arr[j-1] = a


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    rotate(arr, n)
    print(*arr)


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4 


Example 2:
Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1
'''