#################################################
# String is a valid shuffle of 2 strings or not #
#################################################

def isValidShuffle(first, second, result):
    '''
    Function that checks whether a string is a valid shuffle of 2 strings or not
    '''
    if len(first) + len(second) != len(result):
        return False
    else:
        first = ''.join(sorted(first))
        second = ''.join(sorted(second))
        result = ''.join(sorted(result))

        i, j, k = 0, 0, 0

        while k < len(result):
            if i < len(first) and first[i] == result[k]:
                i += 1
            elif j < len(second) and second[j] == result[k]:
                j += 1
            else:
                return False
            k += 1
        
        if i < len(first) and j < len(second):
            return False
        
        return True


def main():
    first, second, result = map(str, input().strip().split())
    print(isValidShuffle(first, second, result))


if __name__ == '__main__':
    main()


'''
Example 1:
Input: abdd fef abfddef
Output: True

Example 2:
Input: aab abc aabbc
Output: False

Example 3:
Input: zxry qwr qwzxxryr
Output: False

Example 4:
Input: xxsz yyy xxyyszy
Output: True
'''