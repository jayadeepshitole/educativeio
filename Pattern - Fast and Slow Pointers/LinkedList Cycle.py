# Given the head of a Singly LinkedList,
# write a function to determine if the LinkedList has a cycle in it or not.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next.next

print(has_cycle(head))