# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        node = root
        if node is not None:
            s = [abs(node.val)]
            if node.left:
                s = self.dfs(node.left) + s
            if node.right:
                s += self.dfs(node.right)
            return s
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = self.dfs(root)
        
        min_diff = float('inf')
        for i in range(1,len(s)):
            this_diff = s[i] - s[i-1]
            if (this_diff < min_diff) and (this_diff != 0):
                min_diff = this_diff
            if min_diff == 1:
                return min_diff
        return min_diff if min_diff != float('inf') else None