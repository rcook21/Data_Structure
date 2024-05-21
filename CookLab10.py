class TreeNode:#Tree Node Class
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BinaryTreeTraversal:
    def __init__(self):
        self.root = None

    def printPreorder(self, node):
        if node is None:#Recursive 
            return

        print(node.data, end=" ")#Print Pre-Order Tree
        self.printPreorder(node.left)
        self.printPreorder(node.right)

    def printInorder(self, node):
        if node is None:#Recursive
            return

        self.printInorder(node.left)#Prints Tree in order
        print(node.data, end=" ")
        self.printInorder(node.right)

    def printPostorder(self, node):#Print Post Order 
        if node is None:#Recursive
            return

        self.printPostorder(node.left)#Sets Node
        self.printPostorder(node.right)
        print(node.data, end=" ")

if __name__ == "__main__":#Binary Tree Numbers
    tree = BinaryTreeTraversal()
    tree.root = TreeNode(4)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(6)
    tree.root.left.left = TreeNode(1)
    tree.root.left.right = TreeNode(3)
    tree.root.right.left = TreeNode(5)
    tree.root.right.right = TreeNode(7)
#Prints Bin Tree pre, in, post order
    print("Pre-order Traversal:", end=" ")
    tree.printPreorder(tree.root)
    print()

    print("In-order Traversal:", end=" ")
    tree.printInorder(tree.root)
    print()

    print("Post-order Traversal:", end=" ")
    tree.printPostorder(tree.root)
    print()