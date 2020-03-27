class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
          print(temp.value, end='')
          temp = temp.next
        print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)

ptr1 = head
ptr2 = head
while ptr2 is not None and ptr2.next is not None:
    ptr1 = ptr1.next
    ptr2 = ptr2.next.next

middle = ptr1
print(middle.value)

# reverse the second half of the linked list
prev_node = None
curr_node = middle
while curr_node is not None:
    next_node = curr_node.next # save next node
    curr_node.next = prev_node # point current next to prev
    prev_node = curr_node # change prev to curr
    curr_node = next_node # change curr to next

prev_node.print_list()

