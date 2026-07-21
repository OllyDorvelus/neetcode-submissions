# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr_node = prev_node = root
        new_node = TreeNode(val)
        if not root:
            root = new_node
            return root
        while curr_node:
            prev_node = curr_node
            if val < curr_node.val:
                curr_node = curr_node.left
            elif val > curr_node.val:
                curr_node = curr_node.right
        if val > prev_node.val:
            prev_node.right = new_node
        else:
            prev_node.left = new_node
        return root