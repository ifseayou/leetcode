# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def dfs(root, currsum, valuelist):
            if root.left==None and root.right==None:
                if currsum==sum: res.append(valuelist)
            if root.left:
                dfs(root.left, currsum+root.left.val, valuelist+[root.left.val])
            if root.right:
                dfs(root.right, currsum+root.right.val, valuelist+[root.right.val])
        
        res=[]
        if root==None: return []
        dfs(root, root.val, [root.val])
        return res