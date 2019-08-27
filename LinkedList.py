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
            return

        while temp is not None:
            if temp.value == key:
                break
            prev = temp
            temp = temp.next


        if temp is None:
            return print('there is no such number')

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while temp:
            print("%d" % (temp.value)),
            temp = temp.next

    def reverse(self):
        current = self.head
        nextNode = None
        previous = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        self.head = previous

    def removeKthNodeFromEnd(self, k):
        prev = node = temp = self.head
        i = 0
        while node:
            node = node.next
            i += 1
        node = self.head
        position = i - k
        if position == 0:
            node = node.next
        else:
            j = 0
            while temp:
                if j == position:
                    break
                j += 1
                prev = temp
                temp = temp.next
            prev.next = prev.next.next


llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.removeKthNodeFromEnd(3)
llist.printList()
