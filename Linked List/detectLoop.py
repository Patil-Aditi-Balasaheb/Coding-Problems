##############################
# Detect loop in Linked List #
##############################

'''
Approach 1: Using Hashing
The idea is to insert the nodes in the hashmap and whenever a node is 
encountered that is already present in the hashmap then return true.
Time complexity: O(N), Only one traversal of the loop is needed.
Auxiliary Space: O(N), N is the space required to store the value in the hashmap.

Approach 2: Using Floyd’s Cycle-Finding Algorithm
This algorithm is used to find a loop in a linked list. 
It uses two pointers one moving twice as fast as the other one. 
The faster one is called the faster pointer and the other one is called the slow pointer.
Time complexity: O(N), Only one traversal of the loop is needed.
Auxiliary Space: O(1).

Approach 3: By Modification In Node Structure
The idea is to modify the node structure by adding flag in it and 
mark the flag whenever visit the node.
Time complexity: O(N), Only one traversal of the loop is needed.
Auxiliary Space: O(1)

Approach 4: By Modifying Value
The idea is to modify the value of the visited node and check if 
current nodes value is equal to that value or not.
Time Complexity: O(N)
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
    
    def detectLoop(self, head):
        '''
        Method to check if the linked list has a loop
        '''
        # # Approach 1: Using hashing
        # visited = set()
        # while head != None:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False

        # Approach 2: Using Floyd’s Cycle-Finding Algorithm
        slow_pointer = fast_pointer = head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
    

def main():
    for _ in range(int(input())):
        n = int(input())
        ll = LinkedList()

        for i in input().split():
            ll.insert(i)

        ll.loopHere(int(input()))
        print(ll.detectLoop(ll.head))


if __name__ == "__main__":
    main()


'''
Example 1:
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output: True
Explanation: In above test case N = 3. The linked list with nodes N = 3 is
given. Then value of x=2 is given which means last node is connected with xth
node of linked list. Therefore, there exists a loop.


Example 2:
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output: False
Explanation: For N = 4 ,x = 0 means then lastNode->next = NULL, then
the Linked list does not contains any loop.
'''