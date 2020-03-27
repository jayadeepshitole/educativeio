class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

ptr1 = head
ptr2 = head

while ptr2 is not None and ptr2.next is not None:
    ptr1 = ptr1.next
    ptr2 = ptr2.next.next

print(ptr1.value)

