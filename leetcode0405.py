# Problem Link : https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def traverse(root, num):
            if root == None:
                return num
            
            nums = num * 10 + root.val
            if root.left == None and root.right == None:
                return nums
            r = 0
            l = 0
            if root.right != None:
                r = traverse(root.right, nums)
            if root.left != None:
                l = traverse(root.left, nums)
            return r + l
            
            
        
        ans = traverse(root, 0)
        return ans