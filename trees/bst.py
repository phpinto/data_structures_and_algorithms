class Node:
    def __init__(self, data):
            self.right = None
            self.left = None
            self.data = data

    def insert(self, val):
        if val <= self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def contains(self, val):
        if val == self.data:
            return True
        elif val < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(val)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print(self.data)

        if self.right is not None:
            self.right.print_in_order()