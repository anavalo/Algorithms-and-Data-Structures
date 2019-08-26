from Node import Node



class LinkedList:
    def __init__(self):
        self.head = None

    def containsNodeWithValue(self, key):
        node = self.head
        while node is not None and node.value != key:
            node = node.next
        return node is not None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        temp = self.head
        prev = None

        if temp.value == key:
            self.head = temp.next
            temp = None
            return "deleted head " + str(key) + " from list"

        while temp.value != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return "no match"

        prev.next = temp.next
        temp = None
        return "deleted " + str(key) + "from list"

    def printList(self):
        temp = self.head
        while temp:
            print(" %d" % (temp.value)),
            temp = temp.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.printList()
llist.remove(5)
print('-------------')
llist.printList()




