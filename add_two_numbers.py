class Node:
    #constructor initialize node object
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_root(self):
        return self.root
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True #data removed
        else:
            prev_node = thiis_node
            this_node = this_node.get_next()
        return False #data not found

    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
        else:
            this_node = this_node.get_next()
        return None




def test(name,expected, actual):
    if expected == actual:
        print('pass: ', name)
    else:
        print('fail: ', name)
        print("expected:", expected)
        print("actual:", actual)

l1 = LinkedList()

name = "get size of LinkedList"
expected = 0
actual = l1.get_size()
test(name, expected, actual)

name = "data in node"
expected = 10
actual = Node(10).get_data()
test(name, expected, actual)

name = "get root of LinkedList"
expected = None
actual = l1.get_root()
test(name, expected, actual)

name = "get root of LinkedList"
expected = None
actual = l1.get_root()
test(name, expected, actual)
