# Problem Link : https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr == None:
                continue
            curr.left, curr.right = curr.right, curr.left
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)   
        return root