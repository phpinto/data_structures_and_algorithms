from linked_list import LinkedList, Node

def reverse_in_place(linked_list):
    prev = None
    curr = linked_list.head
    
    while (curr is not None):
        next_node = curr.get_next()
        curr.set_next(prev)
        prev = curr
        curr = next_node
    linked_list.head = prev

linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(12)
linked_list.insert(10)
linked_list.insert(5)
linked_list.insert(1)
linked_list.insert(56)

print(linked_list)
reverse_in_place(linked_list)
print(linked_list)