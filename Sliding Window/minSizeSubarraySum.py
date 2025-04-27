"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Level: medium
"""
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0 #left pointer
        total = 0
        minArray = math.inf

        for r in range(len(nums)): #move right pointer and add to sum
            total += nums[r]
            while total >= target: #while sum satisfies the condition
                minArray = min(minArray, r-l+1) #calculate the length of new array
                #keep shrinking the window to get min length array
                total -= nums[l] 
                l += 1
                
                        
        if minArray == math.inf:
            return 0
        return minArray