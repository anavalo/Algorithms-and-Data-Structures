'''
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a
simple tree-like structure. Implement the breadthFirstSearch method on the Node class, which takes in an empty array,
 traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
 stores all of the Nodes' names in the input array, and returns it.
'''
from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        current = self.name
        que = deque()
        array.append(current)
        for i in self.children:
            que.append(i)
        while que:
            x = que.popleft()
            array.append(x.name)
            if x.children:
                for i in x.children:
                    que.append(i)
        return array




test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")
print(test4.breadthFirstSearch([]))
