'''
Ryan Cook
CSC 2720
Due Date: 04/09/24
'''

# Define binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteRoot(root):
    if not root:
        return None
    if not root.left:
        return root.right
    if not root.right:
        return root.left

    successor = root.right

    while successor.left:
        successor = successor.left

    root.val = successor.val
    # Delete the successor
    root.right = deleteNode(root.right, root.val)
    return root

def deleteNode(root, key):
    if not root:
        return None
    if root.val == key:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = deleteNode(root.right, root.val)
    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        root.right = deleteNode(root.right, key)
    return root

def inOrderTraversal(root):
    return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right) if root else []

#Test Case 
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root = deleteRoot(root)
print(inOrderTraversal(root)) 