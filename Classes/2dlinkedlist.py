# creating a Two D Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.down = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.down

    def flatten(self):
        root = self.head
        while root:
            if root.down:
                temp = root.down
                while temp.right:
                    temp = temp.right
                temp.right = root.right
            root = root.down

    def printFlattenList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.right

if __name__ == '__main__':
    L = LinkedList()
    L.push(30)
    L.push(8)
    L.push(7)
    L.push(5)

    L.push(20)
    L.push(10)

    L.push(50)
    L.push(22)
    L.push(19)

    L.push(45)
    L.push(40)
    L.push(35)
    L.push(28)

    L.flatten()
    L.printFlattenList()