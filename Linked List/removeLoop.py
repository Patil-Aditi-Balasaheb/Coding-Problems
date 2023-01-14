##############################
# Remove loop in Linked List #
##############################

'''
Optimized Approach: Using Floyd's Cycle finding algorithm without counting nodes in loop
After detecting the loop, if we start the slow pointer from the head and move both slow and fast pointers 
at the same speed until fast don’t meet, they would meet at the beginning of the loop.

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

Explanation - https://youtu.be/qsPoOVAHV_I
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
    
    def length(self):
        '''
        Method that returns the length of Linked list
        '''
        temp = self.head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        return n
    
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
    
    def detectLoop(self, head):
        '''
        Method to check if the linked list has a loop
        '''
        # Using Floyd’s Cycle-Finding Algorithm
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def removeLoop(self, head):
        '''
        Method to remove the loop in a linked list
        '''
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                # special case when both slow and fast pointer meet at head
                if slow == fast:
                    while fast.next != slow:
                        fast = fast.next
                else:
                    while slow.next != fast.next:
                        slow = slow.next
                        fast = fast.next
                fast.next = None
                return 
    

def main():
    for _ in range(int(input())):
        n = int(input())
        ll = LinkedList()

        for i in input().split():
            ll.insert(i)

        ll.loopHere(int(input()))
        print(ll.detectLoop(ll.head))

        ll.removeLoop(ll.head)

        if ll.detectLoop(ll.head) or ll.length() != n:
            print(0)
            continue
        else:
            print(1)


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
N = 3
value[] = {1,3,4}
X = 2

Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it successfully, the answer will be 1. 


Example 2:
Input:
N = 4
value[] = {1,8,3,4}
X = 0

Output: 1
Explanation: The Linked list does not contains any loop. 


Example 3:
Input:
N = 4
value[] = {1,2,3,4}
X = 1

Output: 1
Explanation: The link list looks like 
1 -> 2 -> 3 -> 4
     |_________|
A loop is present. If you remove it successfully, the answer will be 1. 
'''