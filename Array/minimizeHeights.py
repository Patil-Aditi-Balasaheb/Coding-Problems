###################################################
# Minimise the maximum difference between heights #
###################################################

'''
Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.
- Increase the height of the tower by K
- Decrease the height of the tower by K

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
'''

def getMinDiff(arr, n, k):
        # Explanation - https://youtu.be/o9WG7t6EKZo
        arr.sort()                  # sorting the arr
        res = arr[n-1] - arr[0]     # last ele - first ele in sorted array (maximum possible height difference)
        for i in range(1, n):
            # arr[i] - k should not be negative
            if arr[i] >= k:
                minEle = min(arr[i] - k, arr[0] + k)        # arr[i] is y
                maxEle = max(arr[n-1] - k, arr[i-1] + k)    # arr[i-1] is x
                res = min(res, maxEle - minEle)   
        return res


def main():
    k = int(input())
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(getMinDiff(arr, n, k))


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output: 5
Explanation:
The array can be modified as {3, 3, 6, 8}. The difference between the largest and the smallest is 8-3 = 5.

Example 2:
Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation:
The array can be modified as {6, 12, 9, 13, 17}. The difference between the largest and the smallest is 17-6 = 11.
'''