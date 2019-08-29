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
        frontnode = self.head
        endnode = self.head
        counter = 1
        while counter <= k:
            frontnode = frontnode.next
            counter +=1
        if frontnode is None:
            endnode.value = endnode.value.next
            endnode.next = endnode.next.next
            return
        while frontnode is not None:
            temp = endnode
            endnode = endnode.next
            frontnode = frontnode.next
        temp.next = temp.next.next

    def _create_cycle(self):
        node = self.head
        node.next.next.next.next = node.next.next

    def has_cycle(self):
        hash = {}
        node = self.head
        while node:
            if node.next not in hash:
                hash[node.value] = node.next
                prev = node
                node = node.next
            else:
                break
        return print(node.value)


llist = LinkedList()
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
# llist.removeKthNodeFromEnd(4)
llist._create_cycle()
# llist.printList()
llist.has_cycle()
