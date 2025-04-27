"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Level: medium
Approach: sort then backtracking to skip duplicates
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(total, path, start):
            #if reach target
            if total == target:
                return res.append(list(path))
            
            #if exceed target, stop exploring that path
            if total > target:
                return
            
            #explore all possible combinations with numbers starting from after the current element 
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]: #list is sorted, skip duplicates to avoid duplicate combinations
                    continue
                path.append(candidates[i])
                backtrack(total + candidates[i], path, i+1) #start from i+1 so avoid duplicate combinations like [2,3] and [3,2]
                path.pop()
        
        backtrack(0,[],0)
        return res
