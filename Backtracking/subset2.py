"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Level: medium
Approach: sort (to skip duplicates) then backtracking
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(path,start):
            if len(path) == k:
                return ans.append(list(path))
            
            for i in range(start, len(nums)):
                if i>start and nums[i] == nums[i-1]: #Note: i>start not i>0
                    continue
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        
        for k in range(len(nums)+1):
            backtrack([],0)
        
        return ans