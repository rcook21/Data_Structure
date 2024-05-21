class MyLinkedListNode:#Linked List
    def __init__(self, value):#Sets values
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):#Recursive
        self.head = None

    def add(self, value):#Adds function
        if not self.head:
            self.head = MyLinkedListNode(value)
        else:
            current = self.head
            while current.next:#Updates Linked List
                current = current.next
            current.next = MyLinkedListNode(value)

    def display(self):#Display function
        current = self.head
        while current:#While function displays til values is empty
            print(current.value, end=" ")
            current = current.next
        print()

def reverseLinkedList(head: MyLinkedListNode) -> MyLinkedListNode:#Reverse Linked list
    prev = None
    current = head
    while current:#updates list
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Test cases
# Assuming MyLinkedList is implemented as described above

# Test case 1: Normal case
linked_list = MyLinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)

reversed_head = reverseLinkedList(linked_list.head)
reversed_linked_list = MyLinkedList()
reversed_linked_list.head = reversed_head
reversed_linked_list.display()  # Output: 5 4 3 2 1
