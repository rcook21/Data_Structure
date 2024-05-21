'''
Ryan Cook
CSC 2720
Lab Time: 1:00-1:50
Due Date: 2/26/24
'''
class Node:
    def __init__(self, data):
        self.data = data#holds data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):#inserts data into list
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def delete_end(self, n):
        delete = Node(0)
        delete.next = self.head
        fast = slow = delete

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

    def display(self):#displays data
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

#Test Cases
llist = LinkedList()
llist.insert(50)
llist.insert(11)
llist.insert(33)
llist.insert(21)
llist.insert(40)
llist.insert(71)

llist.display()
n = 2#Which int to delete
llist.delete_end(n)
print(f"After deleting the {n} node from the end:")
llist.display()