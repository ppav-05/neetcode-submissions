# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        x = collections.deque()
        x.append(root)

        while x:
            x_len = len(x)
            row = []
            for i in range(x_len):
                node = x.popleft()
                if node:
                    row.append(node.val)
                    x.append(node.left)
                    x.append(node.right)
            if row:
                res.append(row)
        
        return res