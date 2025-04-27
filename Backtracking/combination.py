"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Level: medium
Approach: backtracking
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(path,start):
            if len(path) == k: #if finish 1 combination
                return ans.append(list(path))

            for i in range(start, n+1):
                path.append(i)
                backtrack(path,i+1) #start from i+1 so avoid duplicate combinations like [2,3] and [3,2]
                path.pop()
        
        backtrack([],1)
        return ans