class Node:
    def __init__(self, datavalue = None):
        self.datavalue = datavalue
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, NewNode):
        if self.root is None:
            self.root = Node(NewNode)
        else:
            self._insert(self.root, NewNode)

    def _insert (self, curr_node, NewNode):
        if curr_node.datavalue < NewNode:
            if curr_node.right is None:
                curr_node.right = Node(NewNode)
            else:
                self._insert(curr_node.right, NewNode)
        elif curr_node.datavalue > NewNode:
            if curr_node.left is None:
                curr_node.left = Node(NewNode)
            else:
               self._insert(curr_node.left, NewNode)
        else:
            print("Value aready present")

    def print_tree (self):
        if self.root is not None:
            self.inorder(self.root)
        else:
            print "Tree is empty you idiot"

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.datavalue)
            self.inorder(root.right)

def construct_tree (nodes, bst):
    for i in nodes:
        bst.insert(i)
            
bst = BST()
construct_tree([10, 5, 2, 4, 13, 22, 1, 14], bst)
#construct_tree([8, 3, 10, 1, 6, 14, 4, 7, 13], bst)
#bst.print_tree()

def findClosestValueInBSTRecursive (tree, target):
    return findClosestValueInBSTRecursiveHelper(tree, target, float('inf'))

def findClosestValueInBSTRecursiveHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.datavalue):
        closest = tree.datavalue
    if target < tree.datavalue:
        return findClosestValueInBSTRecursiveHelper(tree.left, target, closest)
    elif target > tree.datavalue:
        return findClosestValueInBSTRecursiveHelper(tree.right, target, closest)
    else:
        return closest

print "Finding closest node for the given target value in a BST using recursive method"
print 'closest node is ' + str(findClosestValueInBSTRecursive(bst.root, 12))

def findClosestValueInBSTIterative (tree, target):
    return findClosestValueInBSTIterativeHelper(tree, target, float('inf'))

def findClosestValueInBSTIterativeHelper(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.datavalue):
            closest = currentNode.datavalue
        if target < currentNode.datavalue:
            currentNode = currentNode.left
        elif target > currentNode.datavalue:
            currentNode = currentNode.right
        else:
            break

    return closest

print "Finding closest node for the given target value in a BST using iterative method"
print 'closest node is ' + str(findClosestValueInBSTIterative(bst.root, 12))
