# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        # if root.left.val != root.right.val:
        #     return False
        return Solution.func(root.left, root.right)

    def func(point_1, point_2):
        if point_1 is None and point_2 is None:
            return True
        if point_1 is None or point_2 is None:
            return False
        if point_1.val == point_2.val:
            ans1 = Solution.func(point_1.left, point_2.right)
            ans2 = Solution.func(point_1.right, point_2.left)
            return ans1 and ans2
        else:
            return False 

        