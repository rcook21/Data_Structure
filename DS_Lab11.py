'''
Ryan Cook
CSC 2720
Lab Time: Friday
Due Date: 03/31/24
'''
from collections import deque

#Bin Tree Node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

#Level Order Traversal
def levelOrder(root):

    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

#Test Case
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5) 
root.right.right = TreeNode(7)
print(levelOrder(root))

#Test Case #2
root1 = TreeNode(1)
print(levelOrder(root1))
# Expected output is [1]