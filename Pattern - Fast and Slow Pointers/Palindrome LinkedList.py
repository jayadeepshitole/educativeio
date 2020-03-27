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


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(2)

# given the head of a ll return the middle node
def find_middle_node(head):
    ptr1 = head
    ptr2 = head
    while ptr2 is not None and ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next

    return ptr1

# reverse the second half of the linked list
def reverse_linked_list(head):
    prev_node = None
    curr_node = head
    while curr_node is not None:
        next_node = curr_node.next # save next node
        curr_node.next = prev_node # point current next to prev
        prev_node = curr_node # change prev to curr
        curr_node = next_node # change curr to next

    return prev_node

# find the middle node and node prev to middle node
middle_node = find_middle_node(head)

# reverse the linked list from the middle
reversed_ll_head = reverse_linked_list(middle_node)

# compare the two ll's now
ll1_ptr, ll2_ptr = head, reversed_ll_head
while ll2_ptr is not None:
    if ll1_ptr.value != ll2_ptr.value:
        print('not palindrome')
        break
    ll1_ptr = ll1_ptr.next
    ll2_ptr = ll2_ptr.next

print('is palindrome')

reverse_linked_list(reversed_ll_head)
head.print_list()
