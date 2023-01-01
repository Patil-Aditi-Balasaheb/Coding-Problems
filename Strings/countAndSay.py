#########################
# Count And Say Problem #
#########################

'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

The first few iterations of the sequence are :
First iteration: “1”
    As we are starting with one.

Second iteration: “11”
    We speak “1” as   “one 1” then we write it as “11”

Third iteration: “21”
    We speak “11” as “Two 1” then we write it as “21”

Fourth iteration: “1211”
    We speak “21” as “one 2, one 1”  then we write it as “1211”

Fifth iteration: “111221”
    We speak “1211” as “one 1, one 2, two 1” then we write it as “111221”

Sixth iteration: “312211”
    We speak “111221” as “three 1, two 2, one 1” then we write it as “312211”

Given a positive integer n, return the nth term of the count-and-say sequence.
'''

def countAndSay(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '11'
    else:
        s = '11'
        for i in range(3, n+1):
            t = ''
            s += '$'
            c = 1
            for j in range(1, len(s)):
                if s[j] != s[j-1]:
                    t += str(c) 
                    t += s[j-1]
                    c = 1
                else:
                    c += 1
            s = t
        return s


def main():
    n = int(input())
    print(countAndSay(n))


if __name__ == '__main__':
    main()


'''
Example 1:
Input: 1
Ouput: 1

Example 2:
Input: 3
Output: 21

Example 3:
Input: 4
Output: 1211

Example 4:
Input: 5
Output: 111221
'''