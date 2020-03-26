# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next.next


def find_cycle_len(head):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast is slow:
            break

    count = 1
    current = slow.next
    while current is not slow:
        current = current.next
        count += 1

    return count

def find_cycle_start(head):
    ptr1 = head
    ptr2 = head
    k = find_cycle_len(head)
    for i in range(k):
        ptr2 = ptr2.next

    while ptr1 is not ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr2.value

print(find_cycle_start(head))

