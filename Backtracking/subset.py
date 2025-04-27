"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Level: medium
Approach: backtracking
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path,start):
            if len(path) == k:
                return ans.append(list(path))
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path,i+1) #start from i+1 so avoid duplicate combinations like [2,3] and [3,2]
                path.pop()
        
        for k in range(len(nums)+1):
            backtrack([],0)
        
        return ans