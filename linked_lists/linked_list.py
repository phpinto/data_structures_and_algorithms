
class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next
        
        def set_data(self, data):
            self.data = data

        def set_next(self, next):
            self.next = next

        def __str__(self):
            return str(self.data)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def get_length(self):
        return self.length

    def insert(self,data,index=0):
        if (index < 0) or (index > self.length):
            return
        insert_node = Node(data)
        if (index == 0):
            if (self.head is None):
                self.head = insert_node
            else:
                insert_node.set_next(self.head)
                self.head = insert_node
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.get_next()
            insert_node.set_next(node.get_next())
            node.set_next(insert_node)
        self.length += 1

    def find(self, data):
        node = self.head
        index = 0
        while (node is not None):
            if (node.data == data): return index
            index += 1
            node = node.get_next()

    def delete(self, index=0):
        if (index < 0) or (index > self.length - 1):
            return
        elif (index == 0):
            self.head = self.head.next
            return
        node = self.head
        if (node is None):
            return
        for _ in range(index - 1):
            node = node.get_next()
        node.next = node.get_next().get_next()
        self.length -= 1

    def __str__(self):
        if self.head is None: return "This list is empty."
        else:
            node = self.head
            ret_list = "["
            while (True):
                ret_list += str(node.data)
                if (node.next is None):
                    ret_list += "]"
                    return ret_list
                else:
                    ret_list += ", "
                    node = node.get_next()