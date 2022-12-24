################################
# Spirally traversing a matrix #
################################

def spiralTraversal(matrix, r, c):
    '''
    Function to return a list of integers denoting spiral traversal of matrix.
    '''
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1
    ans = []

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans


def main():
    r, c = map(int, input().strip().split())
    values = list(map(int, input().strip().split()))
    k = 0
    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(values[k])
            k += 1
        matrix.append(row)

    ans = spiralTraversal(matrix, r, c)
    print(*ans)


if __name__ == '__main__':
    main()


'''
Sample Input 1:
3 4
1 2 3 4 5 6 7 8 9 10 11 12

1 2  3  4 
5 6  7  8 
9 10 11 12

Output:
1 2 3 4 8 12 11 10 9 5 6 7


Sample Input 2:
4 4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

1  2  3  4 
5  6  7  8 
9  10 11 12
13 14 15 16

Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''