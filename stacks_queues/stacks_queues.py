class Stack(object):
    def __init__(self):
        self.data = []

    def get_length(self):
        return len(self.data)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        last = self.data[-1]
        self.data = self.data[:-1]
        return last

    def peek(self):
        return self.data[-1]
    
    def __str__(self):
        return str(self.data)


class Queue(object):
    def __init__(self):
        self.data = []

    def get_length(self):
        return len(self.data)

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        first = self.data[0]
        self.data = self.data[1:]
        return first

    def peek(self):
        return self.data[0]

    def __str__(self):
        return str(self.data)