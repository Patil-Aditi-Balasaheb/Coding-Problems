###########################
# Multiply 2 Linked Lists #
###########################

'''
Given elements as nodes of the two linked lists. The task is to multiply these two linked lists, say L1 and L2. 

Note: The output could be large take modulo 10**9+7.

Time Complexity: O(max(n1, n2)), where n1 and n2 represents the number of nodes present in the first and second linked list respectively.
Auxiliary Space: O(1), no extra space is required, so it is a constant.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    
    def getHead(self):
        return self.head


def multiplyTwoList(head1, head2):
    '''
    Method that multiplies contents of 2 linked list
    '''
    num1 = num2 = 0
    while head1 != None or head2 != None:
        if head1 != None:
            num1 = num1 * 10 + head1.data
            head1 = head1.next

        if head2 != None:
            num2 = num2 * 10 + head2.data
            head2 = head2.next

    return (num1 * num2) % (10 ** 9 + 7)


def main():
    for _ in range(int(input())):
        ll1 = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            ll1.insert(i)
        
        ll2 = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            ll2.insert(i)

        print(multiplyTwoList(ll1.getHead(), ll2.getHead()))


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
2
2
3 2
1
2
3
1 0 0
2
1 0

Output:
64
1000

Explanation:
Testcase 1: 32*2 = 64.
Testcase 2: 100*10 = 1000.


Example 2:
Input:
2
15
8 6 3 1 7 5 9 6 2 1 7 8 5 7 4 
22
9 5 9 7 5 3 8 8 3 1 8 9 6 4 3 3 3 8 6 0 4 8 
29
9 9 7 7 6 4 3 0 3 0 9 2 5 4 0 5 9 4 6 9 2 2 4 7 7 5 4 8 1 
23
9 9 3 6 8 0 2 1 0 5 1 1 0 8 5 0 6 4 6 2 5 8 6

Output:
606331838
589998973
'''