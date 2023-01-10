#########################
# Reverse a Linked List #
#########################

'''
Given a pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

Examples: 
Input: Head of following linked list 1->2->3->4->NULL 
Output: Linked list should be changed to, 4->3->2->1->NULL

Input: Head of following linked list 1->2->3->4->5->NULL 
Output: Linked list should be changed to, 5->4->3->2->1->NULL

Input: NULL 
Output: NULL
'''

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
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
    
    def reverseList(self, head):
        # Approach 1: Iterative Approach
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        # # Approach 2: Recursive Approach
        # if head is None or head.next is None:
        #     return head
        # rest = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return rest
    
    def printList(self, head):
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("NULL")


def main():
    for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        ll = LinkedList()
        for val in arr:
            ll.insert(val)
        
        print("Linked List before reversing:", end=' ')
        ll.printList(ll.head)

        ll.head = ll.reverseList(ll.head)

        print("Linked List after reversing: ", end=' ')
        ll.printList(ll.head)


if __name__ == "__main__":
    main()