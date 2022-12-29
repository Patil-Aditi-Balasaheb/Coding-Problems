######################################
# Median in a row-wise sorted Matrix #
######################################

# Optimized Solution using Binary Search
# Time Complexity - O(n*log(m)) 
# Space Complecity - O(1)

# Solution idea:
# 1. First, we need to find the minimum and maximum elements from the matrix. The minimum and maximum can be easily found since the rows are sorted so we need to compare with the first element of each row for minimum and last element of each row for maximum.
# 2. After finding our min and max, we can apply binary search on this range. The mid element can be calculated and number of elements smaller or equal to mid can be calculated, we have used upper_bound() function for this or countLessThanEqual() in this code solution.
# 3. Based on the value of our counter, the min and max can be adjusted accordingly based on what we do for binary search.


def countLessThanEqual(matrix, r, c, mid):
    '''
    Function to count the number of elements smaller or equal to the mid element
    '''
    cnt = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] > mid:
                break
            else:
                cnt += 1
    
    return cnt


def median(matrix, r, c):
    '''
    Given a row wise sorted matrix of size R*C where R and C are always odd, this function finds the median of the matrix
    '''
    low = 500
    high = -1

    # Finding min and max elements from the matrix
    for i in range(r):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][c-1])

    ans = -1

    while low <= high:
        # Calculate mid
        mid = (low + high) // 2

        # Adjusting min and max based on the count 
        if countLessThanEqual(matrix, r, c, mid) >= ((r * c + 1) // 2):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans


def main():
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t = [int(i) for i in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        
        ans = median(matrix, r, c)
        print(ans)

if __name__ == "__main__":
    main()


'''
Example 1:
Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5
Explanation: Sorting matrix elements gives 
us {1,2,3,3,5,6,6,9,9}. Hence, 5 is median


Example 2:
Input:
R = 3, C = 1
M = [[1], [2], [3]]

Output: 2
Explanation: Sorting matrix elements gives 
us {1,2,3}. Hence, 2 is median.
'''