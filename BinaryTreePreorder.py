# http://oj.leetcode.com/problems/binary-tree-preorder-traversal/
# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        stack = []
        stack.append(root)
        while(len(stack) != 0):
            node = stack.pop()
            if node == None:
                continue
            
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
            
        return result