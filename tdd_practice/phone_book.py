class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data[0] < self.data[0]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data[0] > self.data[0]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.data]
            + self.inorder_traversal(root.right)
        )


class PhoneBook:
    def __init__(self, records=None):
        self.records = records or []

        if len(records) == 1:
            self.records = Node(records[0])
        elif len(records) > 1:
            self.records = Node(records[0])
            for elm in records[1:]:
                self.records.insert(elm)
        else:
            self.records = Node(None)

    def all(self):
        return self.records.inorder_traversal(self.records)

    def add(self, record):
        return self.records.insert(record)
