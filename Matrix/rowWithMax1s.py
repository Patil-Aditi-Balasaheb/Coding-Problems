###################
# Row with max 1s #
###################

'''
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.
'''

# Approach 1 - Brute Force
# A simple method is to do a row-wise traversal of the matrix, 
# count the number of 1s in each row, and compare the count with the max. 
# Finally, return the index of the row with a maximum of 1s. 
# The time complexity of this method is O(n*m) where n is the number of rows and m is the number of columns in the matrix.

# Approach 2 - Binary Search
# We can make use of binary search as the rows are sorted, 
# to find the first occurence (first) of 1 in a row and calculating no. of 1s as (m - first) where m is the number of columns.
# The time complexity of this method is O(n*log(m)) where n is the number of rows and m is the number of columns in the matrix.

# Approach 3 - Linear Time Search
# 1. Get the index of first (or leftmost) 1 in the first row.
# 2. Do following for every row after the first row 
#       …IF the element on left of previous leftmost 1 is 0, ignore this row. 
#       …ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.
# The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.


def rowWithMax1s(matrix, n, m):
    '''
    Function that returns index of row with maximum number of 1s.
    '''
    # Approach 1
    # maxx = 0
    # row = -1
    # for i in range(n):
    #     if matrix[i].count(1) > maxx:
    #         maxx = matrix[i].count(1)
    #         row = i
    # return row 


    # Approach 3
    row = -1
    j = m - 1

    for i in range(n):
        flag = False
        while j >= 0 and matrix[i][j] == 1:
            j -= 1
            flag = True

        if flag:
            row = i
        
    return row


def main():
    n, m = map(int, input().strip().split())
    inputLine = list(map(int, input().strip().split()))

    matrix = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = inputLine[i * m + j]
    
    ans = rowWithMax1s(matrix, n, m)
    print(ans)


if __name__ == '__main__':
    main()


'''
Example 1:
Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}

Output: 2
Explanation: Row 2 contains 4 1's (0-based indexing).


Example 2:
Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}

Output: 1
Explanation: Row 1 contains 2 1's (0-based indexing).
'''