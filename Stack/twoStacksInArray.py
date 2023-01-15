##########################
# Two Stacks in an Array #
##########################

'''
Design a data structure, which represents two stacks using only one array common for both stacks. 

The data structure should support the following operations:
- push1(NUM) - Push ‘NUM’ into stack1.
- push2(NUM) - Push ‘NUM’ into stack2.
- pop1() - Pop out a top element from stack1 and return popped element, in case of underflow return -1.
- pop2() - Pop out a top element from stack2 and return popped element, in case of underflow return -1.

There are 2 types of queries in the input:
- Type 1 - These queries correspond to Push operation.
- Type 2 - These queries correspond to Pop operation.

Solution Approach:
Implement two stacks in an array by Starting from endpoints:
The idea is to start two stacks from two extreme corners of arr[]. 

Follow the steps below to solve the problem:
- Stack1 starts from the leftmost corner of the array, the first element in stack1 is pushed at index 0 of the array. 
- Stack2 starts from the rightmost corner of the array, the first element in stack2 is pushed at index (n-1) of the array. 
- Both stacks grow (or shrink) in opposite directions. 
- To check for overflow, all we need to check is for availability of space between top elements of both stacks.
- To check for underflow, all we need to check is if the value of the top of the both stacks is between 0 to (n-1) or not.

Time Complexity: 
Both Push operation: O(1)
Both Pop operation: O(1)

Auxiliary Space: O(N), Use of the array to implement stack.
'''

top1 = -1
top2 = 101

def push1(a, x):
    '''
    Function to push an integer into the stack1
    '''
    global top1, top2
    # Check if there is at least one empty space for new element
    if top1 < top2 - 1:
        top1 += 1
        a[top1] = x


def push2(a, x):
    '''
    Function to push an integer into the stack2
    '''
    global top1, top2
    # Check if there is at least one empty space for new element
    if top1 < top2 - 1:
        top2 -= 1
        a[top2] = x


def pop1(a):
    '''
    Function to remove an element from top of the stack1
    '''
    global top1
    if top1 >= 0:
        x = a[top1]
        top1 -= 1
        return x
    return -1


def pop2(a):
    '''
    Function to remove an element from top of the stack2
    '''
    global top2
    if top2 < len(a):
        x = a[top2]
        top2 += 1
        return x
    return -1


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        a = [-1] * n  # array to be used for the 2 stacks
        i = 0
        global top2
        top2 = n
        while i < len(arr):
            if arr[i] == 1:
                if arr[i+1] == 1:
                    push1(a, arr[i+2])
                    i += 1
                else:
                    print(pop1(a), end=" ")
                i += 1
            else:
                if arr[i+1] == 1:
                    push2(a, arr[i+2])
                    i += 1
                else:
                    print(pop2(a), end=" ")
                i += 1
            i += 1
        print()

   
if __name__ == "__main__":
    main()


'''
Input Format:
First line contains an integer Q denoting the number of queries . 
A Query Q is of 4 Types
(i)    1 1 x   (a query of this type means  pushing 'x' into the stack 1)
(ii)   1 2     (a query of this type means to pop element from stack1  and print the poped element)
(iii)  2 1 x   (a query of this type means pushing 'x' into the stack 2)
(iv)   2 2     (a query of this type means to pop element from stack2 and print the poped element)
The second line contains Q queries seperated by space.


Example 1:
Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()

Actual Input:
1   # no of test cases
6   # size of array
1 1 2 1 1 3 2 1 4 1 2 2 2 2 2   # operations

Output:
3 4 -1

Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence -1.
'''