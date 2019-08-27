class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse(self, head):
        current = head
        nextNode = None
        previous = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode


    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
print("Initial list: ")
testHead.printList()
testHead.reverse(testHead)
print("REVERSED list: ")
testHead.printList()