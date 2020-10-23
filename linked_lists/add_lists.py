#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def add_lists(first, second):
    
    reversed_first, reversed_second = None, None

    while(first is not None or second is not None):
        if (first is not None):
            if reversed_first is None:
                prev_first = reversed_first
                reversed_first = Node(first.data)
            else:
                prev_first = Node(reversed_first.data)
                prev_first.next = reversed_first.next
                reversed_first.data = first.data
                reversed_first.next = prev_first
    
            first = first.next

        if (second is not None):
            if reversed_second is None:
                prev_second = reversed_second
                reversed_second = Node(second.data)
            else:
                prev_second = Node(reversed_second.data)
                prev_second.next = reversed_second.next
                reversed_second.data = second.data
                reversed_second.next = prev_second
            second = second.next
    
    sum_list = []
    sumLL = LinkedList()
    carry_over = 0
    
    while (reversed_first is not None or reversed_second is not None):
        first_val, second_val = 0,0
        
        if reversed_first is not None:
            first_val = reversed_first.data
            reversed_first = reversed_first.next
            
        if reversed_second is not None:
            second_val = reversed_second.data
            reversed_second = reversed_second.next
            
        this_sum = first_val + second_val + carry_over
        
        if this_sum >= 10:
            carry_over = 1
            this_sum -= 10
        else:
            carry_over = 0
        sum_list.append(this_sum)
    
    if carry_over > 0:
        sumLL.insert(carry_over)

    for i in range(-1,-len(sum_list) - 1,-1):
        sumLL.insert(sum_list[i])   
    return sumLL
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

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

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':

    arr1 = [7,7,0,3,2]
    LL1 = LinkedList()
    for i in arr1:
        LL1.insert(i)
    
    arr2 = [2,9,6,6,0]
    LL2 = LinkedList()
    for i in arr2:
        LL2.insert(i)
    
    res = add_lists(LL1.head, LL2.head)
    printList(res.head)
