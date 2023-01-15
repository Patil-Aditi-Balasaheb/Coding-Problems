##########################################
# Find first node of loop in Linked List #
##########################################

'''
Optimized Approach: Using Floyd's Cycle finding algorithm without counting nodes in loop
Below are steps to find the first node of the loop.
1. If a loop is found, initialize a slow pointer to head, let fast pointer be at its position. 
2. Move both slow and fast pointers one node at a time. 
3. The point at which they meet is the start of the loop.

Distance traveled by fast pointer = 2 * (Distance traveled by slow pointer)
(m + n*x + k) = 2 * (m + n*y + k)

Note that before meeting the point shown above, fast was moving at twice speed.
x -->  Number of complete cyclic rounds made by fast pointer before they meet first time
y -->  Number of complete cyclic rounds made by slow pointer before they meet first time

From the above equation, we can conclude m + k = (x - 2y) * n

Which means m + k is a multiple of n. 
Thus we can write, m + k = i * n or m = i * n - k.
Hence, distance moved by slow pointer: m, is equal to distance moved by fast pointer:
i * n - k or (i - 1) * n + n - k (cover the loop completely i-1 times and start from n-k).

Time Complexity: O(N), Where N is the number of nodes in the list
Auxiliary Space: O(1)
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
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    
    def loopHere(self, pos):
        '''
        Method that connects last node to node at position pos from beginning
        '''
        if pos == 0:
            return
        temp = self.head
        for i in range(1, pos):
            temp = temp.next
        self.tail.next = temp

    def findFirstNode(self, head):
        '''
        Method to find first node if the linked list has a loop
        '''
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast.data
        return -1   # if no loop present
    

def main():
    for _ in range(int(input())):
        n = int(input())
        ll = LinkedList()

        for i in input().split():
            ll.insert(i)

        ll.loopHere(int(input()))
        print(ll.findFirstNode(ll.head))


if __name__ == "__main__":
    main()


'''
Example:
Input:
3               # no. of test cases
5               # size of linked list
1 3 2 4 5       # linked list elements
2               # loop 2nd node
3               # output - first loop node with value 3
4               # size of linked list
1 3 2 1         # linked list elements
0               # no loop
-1              # output - no loop hence return -1
5               # size of linked list
3 2 0 -4 -1     # linked list elements
3               # loop 3rd node               
0               # output - first loop node with value 0
'''