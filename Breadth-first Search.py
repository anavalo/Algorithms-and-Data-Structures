'''
You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a
simple tree-like structure. Implement the breadthFirstSearch method on the Node class, which takes in an empty array,
 traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
 stores all of the Nodes' names in the input array, and returns it.
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        child = self.children
        hash = {}
        for i in range(len(child)):
            hash[child[i]] = self.name


test1 = Node('A')
test1.addChild('B').addChild('C')
test1.children[0].addChild('D')

