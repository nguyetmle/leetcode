"""
Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Level: medium
Approach: dfs/backtracking
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def backtrack(root,remaining,path):
            #base case: finish one branch
            if not root:
                return
            
            # Add the current node to the path's list
            path.append(root.val)

            # Check if the current node is a leaf and also, if it
            # equals our remaining sum. If it does, we add the path to
            # our list of paths
            if root.val == remaining and not root.left and not root.right:
                ans.append(list(path))
            else: 
                # Else, we will recurse on the left and the right children
                backtrack(root.left, remaining - root.val, path)
                backtrack(root.right, remaining - root.val, path)

            # We need to pop the node once we are done processing ALL of it's
            # subtrees.
            path.pop()

   
        backtrack(root,targetSum,[])
        return ans
