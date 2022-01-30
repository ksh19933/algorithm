# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        nodes = deque()
        nodes.append(root)
        while nodes:
            node: TreeNode = nodes.popleft()
            node.left, node.right = node.right ,node.left
            if node.right != None:
                nodes.append(node.right)
            if node.left != None:
                nodes.append(node.left)
        return root



