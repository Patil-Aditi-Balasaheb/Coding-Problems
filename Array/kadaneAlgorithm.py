########################################################
# Kadane's Algorithm (Largest Sum Contiguous Subarray) #
########################################################

'''
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum
'''

def maxSubArraySum(arr,N):
    max_sum = arr[0]
    max_till_now = 0 if arr[0] < 0 else arr[0]
    for i in range(1, N):
        max_till_now += arr[i]
        max_sum = max(max_sum, max_till_now)
        if max_till_now < 0:
            max_till_now = 0
    return max_sum


def main():
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(maxSubArraySum(arr, n))


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output: 9
Explanation:
Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Example 2:
Input:
N = 4
Arr[] = {-1,-2,-3,-4}
Output: -1
Explanation:
Max subarray sum is -1 of element (-1)
'''